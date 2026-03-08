import pickle
import numpy as np
from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"

# ---------------------------
# Load ML Model
# ---------------------------
model = pickle.load(open("model/demand_model.pkl", "rb"))


# ---------------------------
# Database Initialization
# ---------------------------
def init_db():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        name TEXT,
        email TEXT PRIMARY KEY,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()


# Run database initialization
init_db()


# ---------------------------
# Database Connection
# ---------------------------
def get_db():
    conn = sqlite3.connect("database.db")
    return conn


# ---------------------------
# Login Page
# ---------------------------
@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, password)
        )

        user = cursor.fetchone()

        if user:
            session["user"] = email
            return redirect("/dashboard")

        else:
            return render_template("login.html", error="Invalid Credentials")

    return render_template("login.html")


# ---------------------------
# Signup Page
# ---------------------------
@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db()
        cursor = conn.cursor()

        try:

            cursor.execute(
                "INSERT INTO users VALUES (?,?,?)",
                (name, email, password)
            )

            conn.commit()

            return redirect("/")

        except:
            return render_template("signup.html", error="User already exists")

    return render_template("signup.html")


# ---------------------------
# Dashboard
# ---------------------------
@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/")

    return render_template("dashboard.html")


# ---------------------------
# Prediction Route
# ---------------------------
@app.route("/predict", methods=["POST"])
def predict():

    if "user" not in session:
        return redirect("/")

    store = int(request.form["store"])
    item = int(request.form["item"])
    sales = int(request.form["sales"])
    promo = int(request.form["promo"])

    features = np.array([[store, item, sales, promo]])

    prediction = model.predict(features)

    return render_template(
        "dashboard.html",
        prediction=int(prediction[0])
    )


# ---------------------------
# Logout
# ---------------------------
@app.route("/logout")
def logout():

    session.pop("user", None)

    return redirect("/")


# ---------------------------
# Run App
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True)
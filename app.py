import pickle
import sqlite3
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "inventory_secret_key"


# LOAD MODEL
with open("model/demand_model.pkl", "rb") as f:
    model = pickle.load(f)


# DATABASE CONNECTION
def get_db():
    conn = sqlite3.connect("database/database.db")
    conn.row_factory = sqlite3.Row
    return conn


# HOME
@app.route("/")
def home():
    return redirect("/login")


# REGISTER
@app.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db()

        conn.execute(
            "INSERT INTO users(name,email,password) VALUES (?,?,?)",
            (name,email,password)
        )

        conn.commit()

        return redirect("/login")

    return render_template("register.html")


# LOGIN
@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        conn = get_db()

        user = conn.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email,password)
        ).fetchone()

        if user:

            session["user_id"] = user["id"]

            return redirect("/dashboard")

    return render_template("login.html")


# DASHBOARD
@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect("/login")

    return render_template("dashboard.html",
                           demand="--",
                           stock="--",
                           reorder="--")


# INVENTORY CHECK
@app.route("/predict", methods=["POST"])
def predict():

    current_stock = int(request.form["stock"])

    base_features = [
        current_stock,
        60,
        55.0,
        120.0,
        10,
        1,
        115.0,
        15,
        6,
        2024
    ]

    remaining = [0]*(model.n_features_in_ - len(base_features))

    final_input = base_features + remaining

    prediction = model.predict([final_input])[0]

    reorder_point = 600

    reorder = "YES" if current_stock < reorder_point else "NO"

    return render_template("dashboard.html",
                           demand=round(prediction,2),
                           stock=current_stock,
                           reorder=reorder)


# LOGOUT
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)
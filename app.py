import os
import pickle
import sqlite3
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "inventory_secret_key"


# LOAD MODEL
try:
    with open("model/demand_model.pkl", "rb") as f:
        model = pickle.load(f)
except Exception as e:
    print("Model loading error:", e)
    model = None


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
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        # empty input validation
        if not name or not email or not password:
            return render_template("register.html", error="All fields are required")

        conn = get_db()

        try:
            conn.execute(
                "INSERT INTO users(name,email,password) VALUES (?,?,?)",
                (name, email, password)
            )
            conn.commit()

        except sqlite3.IntegrityError:
            return render_template("register.html", error="Email already registered")

        return render_template("login.html", success="Account created successfully. Please login.")

    return render_template("register.html")


# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            return render_template("login.html", error="Please enter email and password")

        conn = get_db()

        user = conn.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, password)
        ).fetchone()

        if not user:
            return render_template("login.html", error="Invalid email or password")

        session["user_id"] = user["id"]

        return redirect("/dashboard")

    return render_template("login.html")


# DASHBOARD
@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect("/login")

    return render_template(
        "dashboard.html",
        demand="--",
        stock="--",
        reorder="--"
    )


# INVENTORY CHECK
@app.route("/predict", methods=["POST"])
def predict():

    if "user_id" not in session:
        return redirect("/login")

    stock = request.form.get("stock")

    # empty stock validation
    if not stock:
        return render_template(
            "dashboard.html",
            error="Please enter stock value",
            demand="--",
            stock="--",
            reorder="--"
        )

    # invalid number validation
    try:
        current_stock = int(stock)
    except ValueError:
        return render_template(
            "dashboard.html",
            error="Stock must be a number",
            demand="--",
            stock="--",
            reorder="--"
        )

    # prediction
    try:

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

        remaining = [0] * (model.n_features_in_ - len(base_features))

        final_input = base_features + remaining

        prediction = model.predict([final_input])[0]

    except Exception as e:

        print("Prediction error:", e)

        return render_template(
            "dashboard.html",
            error="Prediction failed",
            demand="--",
            stock=current_stock,
            reorder="Error"
        )

    reorder_point = 600
    reorder = "YES" if current_stock < reorder_point else "NO"

    return render_template(
        "dashboard.html",
        demand=round(prediction, 2),
        stock=current_stock,
        reorder=reorder
    )


# LOGOUT
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


# IMPORTANT FOR RENDER DEPLOYMENT
if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=port)
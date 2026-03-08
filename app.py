import pickle
from flask import Flask, render_template, request

# -------- CREATE FLASK APP --------
app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

# -------- LOAD MODEL SAFELY --------
try:
    with open("model/demand_model.pkl", "rb") as f:
        model = pickle.load(f)
except Exception as e:
    print("Error loading model:", e)
    model = None


# -------- HOME PAGE --------
@app.route("/")
def home():
    return render_template(
        "index.html",
        demand="--",
        stock="--",
        reorder="--"
    )


# -------- CHECK INVENTORY --------
@app.route("/check", methods=["POST"])
def check_inventory():

    # Handle user input safely
    try:
        current_stock = int(request.form["stock"])
    except ValueError:
        return render_template(
            "index.html",
            demand="Invalid Input",
            stock="Invalid Input",
            reorder="Enter numeric value"
        )

    # Features used by ML model
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

    remaining_features = [0] * (model.n_features_in_ - len(base_features))
    final_input = base_features + remaining_features

    # Prediction
    try:
        predicted_demand = model.predict([final_input])[0]
    except Exception as e:
        return render_template(
            "index.html",
            demand="Prediction Error",
            stock=current_stock,
            reorder="Model issue"
        )

    # Reorder logic
    reorder_point = 600
    reorder_status = "YES" if current_stock < reorder_point else "NO"

    return render_template(
        "index.html",
        demand=round(predicted_demand, 2),
        stock=current_stock,
        reorder=reorder_status
    )


# -------- RUN APP --------
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
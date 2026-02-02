import pickle
from flask import Flask, render_template, request

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

# Load trained ML model
with open("model/demand_model.pkl", "rb") as f:
    model = pickle.load(f)

# ---------------- HOME PAGE ----------------
@app.route("/")
def home():
    return render_template(
        "index.html",
        demand="--",
        stock="--",
        reorder="--"
    )

# ---------------- CHECK INVENTORY ----------------
@app.route("/check", methods=["POST"])
def check_inventory():

    current_stock = int(request.form["stock"])

    # Base features (same order as training)
    base_features = [
        current_stock,   # Inventory Level
        60,              # Units Ordered
        55.0,            # Demand Forecast
        120.0,           # Price
        10,              # Discount
        1,               # Holiday / Promotion
        115.0,           # Competitor Pricing
        15,              # Day
        6,               # Month
        2024             # Year
    ]

    remaining_features = [0] * (model.n_features_in_ - len(base_features))
    final_input = base_features + remaining_features

    predicted_demand = model.predict([final_input])[0]

    reorder_point = 600
    reorder_status = "YES" if current_stock < reorder_point else "NO"

    return render_template(
        "index.html",
        demand=round(predicted_demand, 2),
        stock=current_stock,
        reorder=reorder_status
    )

# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)

from flask import Flask, render_template, request, redirect
from models import db, User
from optimizer.inventory_logic import analyze_inventory

app = Flask(__name__)

# DATABASE CONFIG
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

inventory_df = None

stats = {
    "total": 0,
    "low_stock": 0,
    "overstock": 0,
    "supplier_delay": 0
}


# LOGIN PAGE
@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if not user:

            return render_template(
                "login.html",
                error="User not registered. Please register first."
            )

        if user.password != password:

            return render_template(
                "login.html",
                error="Incorrect password"
            )

        return redirect("/dashboard")

    return render_template("login.html")


# REGISTER PAGE
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:

            return render_template(
                "register.html",
                error="User already registered"
            )

        new_user = User(
            username=username,
            email=email,
            password=password
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect("/")

    return render_template("register.html")


# DASHBOARD PAGE
@app.route("/dashboard")
def dashboard():

    return render_template(
        "dashboard.html",
        stats=stats
    )


# CSV ANALYSIS
@app.route("/analyze", methods=["POST"])
def analyze():

    global inventory_df
    global stats

    if "file" not in request.files:

        return "No file uploaded"

    file = request.files["file"]

    if file.filename == "":

        return "No file selected"

    try:

        result = analyze_inventory(file)

        inventory_df = result["data"]

        stats = result

    except Exception as e:

        return f"CSV error: {str(e)}"

    return redirect("/dashboard")


# PRODUCT STATUS CHECK FEATURE (NEW)
@app.route("/check_product", methods=["POST"])
def check_product():

    global inventory_df

    if inventory_df is None:

        return redirect("/dashboard")

    product_name = request.form["product_name"].lower()

    df = inventory_df.copy()

    df.columns = df.columns.str.lower()

    product = df[df["product_name"].str.lower() == product_name]

    if product.empty:

        return render_template(
            "dashboard.html",
            stats=stats,
            result="❌ Product not found"
        )

    stock = int(product.iloc[0]["stock_quantity"])
    reorder = int(product.iloc[0]["reorder_level"])
    lead_time = int(product.iloc[0]["lead_time_days"])

    if lead_time > 10:

        message = "🚚 Supplier delay risk detected"

    elif stock <= reorder:

        message = "⚠ Low stock — restock required"

    elif stock > 150:

        message = "📦 Overstock detected"

    else:

        message = "✅ Product available in stock"

    return render_template(
        "dashboard.html",
        stats=stats,
        result=message
    )


# PRODUCTS TABLE PAGE
@app.route("/products")
def products():

    global inventory_df

    if inventory_df is None:

        return redirect("/dashboard")

    data = inventory_df.to_dict(orient="records")

    return render_template(
        "products.html",
        products=data
    )


# VISUAL PAGE
@app.route("/visuals")
def visuals():

    global inventory_df
    global stats

    if inventory_df is None:

        return render_template(
            "visuals.html",
            stats=None,
            categories=None
        )

    # category-wise count
    category_data = (
        inventory_df["category"]
        .value_counts()
        .to_dict()
    )

    return render_template(
        "visuals.html",
        stats=stats,
        categories=category_data
    )
# SETTINGS PAGE
@app.route("/settings")
def settings():

    return render_template("settings.html")


# LOGOUT
@app.route("/logout")
def logout():

    return redirect("/")


# RUN APP
if __name__ == "__main__":

    with app.app_context():

        db.create_all()

    app.run(debug=True)
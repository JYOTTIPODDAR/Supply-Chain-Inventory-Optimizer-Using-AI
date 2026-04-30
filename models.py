from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100))

    email = db.Column(db.String(120), unique=True)

    password = db.Column(db.String(100))

    # SETTINGS FIELDS
    low_stock_threshold = db.Column(
        db.Integer,
        default=10
    )

    reorder_quantity = db.Column(
        db.Integer,
        default=50
    )

    email_alerts = db.Column(
        db.Boolean,
        default=True
    )

    auto_reorder = db.Column(
        db.Boolean,
        default=False
    )
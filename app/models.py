from app import db

class Rental(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    rent_price = db.Column(db.Float, nullable=False)
    billing_date = db.Column(db.String(50))
    status = db.Column(db.String(20), default="Available")

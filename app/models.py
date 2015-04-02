from app import db

class items(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), nullable=False)
	description = db.Column(db.String(120), nullable=False)
from wall.database import db
import datetime

class Stories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.String(100), nullable=False)
    current_date = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class Replies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    parent_id = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.String(100), nullable=False)
    current_date = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
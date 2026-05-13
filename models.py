from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))

class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    sleeping = db.Column(db.Integer)
    exercise = db.Column(db.Integer)
    study_hours = db.Column(db.Integer)
    screen_time = db.Column(db.Integer)

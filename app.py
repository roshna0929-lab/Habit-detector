from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['JWT_SECRET_KEY'] = 'secretkey'

CORS(app)

db = SQLAlchemy(app)
jwt = JWTManager(app)

from models import User, Habit

@app.route('/')
def home():
    return {"message": "Habit Tracker Backend Running"}

# Signup
@app.route('/signup', methods=['POST'])
def signup():
    from flask import request
    from werkzeug.security import generate_password_hash

    data = request.get_json()

    username = data['username']
    password = generate_password_hash(data['password'])

    user = User(username=username, password=password)

    db.session.add(user)
    db.session.commit()

    return {"message": "User created successfully"}

# Login
@app.route('/login', methods=['POST'])
def login():
    from flask import request
    from werkzeug.security import check_password_hash
    from flask_jwt_extended import create_access_token

    data = request.get_json()

    user = User.query.filter_by(username=data['username']).first()

    if user and check_password_hash(user.password, data['password']):
        token = create_access_token(identity=user.id)
        return {"token": token}

    return {"message": "Invalid credentials"}, 401

# Save Habit Survey
@app.route('/habit', methods=['POST'])
def save_habit():
    from flask import request

    data = request.get_json()

    habit = Habit(
        user_id=data['user_id'],
        sleeping=data['sleeping'],
        exercise=data['exercise'],
        study_hours=data['study_hours'],
        screen_time=data['screen_time']
    )

    db.session.add(habit)
    db.session.commit()

    return {"message": "Habit saved successfully"}

# Weekly Report
@app.route('/weekly/<int:user_id>')
def weekly_report(user_id):
    habits = Habit.query.filter_by(user_id=user_id).all()

    total_sleep = 0
    total_exercise = 0

    for h in habits:
        total_sleep += h.sleeping
        total_exercise += h.exercise

    return {
        "average_sleep": total_sleep / len(habits) if habits else 0,
        "average_exercise": total_exercise / len(habits) if habits else 0
    }

# Admin Dashboard
@app.route('/admin/stats')
def admin_stats():
    total_users = User.query.count()
    total_surveys = Habit.query.count()

    return {
        "total_users": total_users,
        "total_surveys": total_surveys
    }

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)

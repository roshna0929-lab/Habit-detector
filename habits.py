from flask import Blueprint, request
from models import db, Habit

habits = Blueprint('habits', __name__)

@habits.route('/habit', methods=['POST'])
def add_habit():
    data = request.get_json()

    new_habit = Habit(
        user_id=data['user_id'],
        sleeping=data['sleeping'],
        exercise=data['exercise'],
        study_hours=data['study_hours'],
        screen_time=data['screen_time']
    )

    db.session.add(new_habit)
    db.session.commit()

    return {"message": "Habit saved"}

@habits.route('/weekly/<int:user_id>')
def weekly_report(user_id):
    habits_data = Habit.query.filter_by(user_id=user_id).all()

    total_sleep = 0

    for h in habits_data:
        total_sleep += h.sleeping

    average_sleep = (
        total_sleep / len(habits_data)
        if habits_data else 0
    )

    return {
        "average_sleep": average_sleep
    }

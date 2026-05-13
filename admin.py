from flask import Blueprint
from models import User, Habit

admin = Blueprint('admin', __name__)

@admin.route('/admin/stats')
def stats():
    total_users = User.query.count()
    total_surveys = Habit.query.count()

    return {
        "total_users": total_users,
        "total_surveys": total_surveys
    }

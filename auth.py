from flask import Blueprint, request
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    user = User(
        username=data['username'],
        password=generate_password_hash(data['password'])
    )

    db.session.add(user)
    db.session.commit()

    return {"message": "User created"}

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    user = User.query.filter_by(
        username=data['username']
    ).first()

    if user and check_password_hash(user.password, data['password']):
        token = create_access_token(identity=user.id)
        return {"token": token}

    return {"message": "Invalid credentials"}, 401

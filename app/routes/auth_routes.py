from flask import Blueprint, request, jsonify
from app.model.user import user
import bcrypt

bp = Blueprint('auth', __name__)

@bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data['username']
    email = data['email']
    phone_number = data['phone_number']
    password = data['password']

    if user.get_user_by_email(email):
        return jsonify({"message": "User already exists"}), 409

    user.create_user(username, email, phone_number, password)
    return jsonify({"message": "User created successfully"}), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data['email']
    password = data['password']

    user = user.get_user_by_email(email)
    if not user:
        return jsonify({"message": "User not found"}), 404

    if bcrypt.checkpw(password.encode('utf-8'), user['password_hash'].encode('utf-8')):
        return jsonify({"message": "Login successful", "user_id": user['id']}), 200
    else:
        return jsonify({"message": "Incorrect password"}), 401

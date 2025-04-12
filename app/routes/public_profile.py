from flask import Blueprint, jsonify
from app.model.basic_info import basic_info
from app import db

public_bp = Blueprint('public', __name__)

@public_bp.route('/public/<int:user_id>', methods=['GET'])
def get_public_profile(user_id):
    info = basic_info.query.filter_by(user_id=user_id).first()

    if not info:
        return jsonify({"error": "No public info found"}), 404

    public_data = {
        "name": info.name,
        "age_range": info.age_range,
        "gender": info.gender,
        "allergies": info.known_allergy,
        "chronic_conditions": info.chronic_disease,
        "disability": info.disability,
        "emergency_contact": info.emergency_contact_info
    }

    return jsonify(public_data)

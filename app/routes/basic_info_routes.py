from flask import Blueprint, request, jsonify
from app.model.basic_info import basic_info

bp = Blueprint('basic_info', __name__)

@bp.route('/basic-info/<int:user_id>', methods=['GET'])
def get_basic_info(user_id):
    info = basic_info.get_basic_info(user_id)
    if info:
        return jsonify(info), 200
    else:
        return jsonify({"message": "Basic info not found"}), 404

@bp.route('/basic-info/<int:user_id>', methods=['POST'])
def post_basic_info(user_id):
    data = request.json
    basic_info.save_basic_info(
        user_id=user_id,
        name=data['name'],
        age_range=data['age_range'],
        gender=data['gender'],
        known_allergy=data['known_allergy'],
        chronic_disease=data['chronic_disease'],
        disability=data['disability'],
        emergency_contact_info=data['emergency_contact_info']
    )
    return jsonify({"message": "Basic info saved"}), 201

@bp.route('/basic-info/<int:user_id>', methods=['PATCH'])
def update_basic_info(user_id):
    data = request.json
    updated = basic_info.update_basic_info(user_id, data)
    if updated:
        return jsonify({"message": "Basic info updated"}), 200
    else:
        return jsonify({"message": "Basic info not found"}), 404

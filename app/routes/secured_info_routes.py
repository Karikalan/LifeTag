from flask import Blueprint, request, jsonify
from app.model.secured_info import secured_info

bp = Blueprint('secured_info', __name__)

@bp.route('/secured-info/<int:user_id>', methods=['GET'])
def get_secured_info(user_id):
    # TODO: Add PIN/OTP verification before exposing this data
    info = secured_info.get_secured_info(user_id)
    if info:
        return jsonify(info), 200
    else:
        return jsonify({"message": "Secured info not found"}), 404

@bp.route('/secured-info/<int:user_id>', methods=['POST'])
def post_secured_info(user_id):
    data = request.json
    secured_info.save_secured_info(
        user_id=user_id,
        full_name=data['full_name'],
        medical_history=data['medical_history'],
        medication_in_use=data['medication_in_use'],
        doctor_details=data['doctor_details'],
        exact_age=data['exact_age']
    )
    return jsonify({"message": "Secured info saved"}), 201

@bp.route('/secured-info/<int:user_id>', methods=['PATCH'])
def update_secured_info(user_id):
    data = request.json
    updated = secured_info.update_secured_info(user_id, data)
    if updated:
        return jsonify({"message": "Secured info updated"}), 200
    else:
        return jsonify({"message": "Secured info not found"}), 404

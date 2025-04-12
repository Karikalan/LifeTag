import qrcode
import os
from flask import Blueprint, jsonify, request

qr_bp = Blueprint('qr', __name__)

@qr_bp.route('/generate_qr/<int:user_id>', methods=['GET'])
def generate_qr(user_id):
    public_url = f"http://localhost:5000/public/{user_id}"  # Replace with your domain in production

    # Create QR
    qr_img = qrcode.make(public_url)

    # Save it
    save_path = f"static/qrcodes/user_{user_id}.png"
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    qr_img.save(save_path)

    return jsonify({
        "message": "QR Code generated successfully",
        "qr_image_url": f"/{save_path}"
    })

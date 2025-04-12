from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    
    CORS(app)

    # Register Blueprints
    from app.routes import auth_routes, basic_info_routes, secured_info_routes, qr_routes, public_profile
    app.register_blueprint(auth_routes.bp)
    app.register_blueprint(basic_info_routes.bp)
    app.register_blueprint(secured_info_routes.bp)
    app.register_blueprint(qr_routes.qr_bp)
    app.register_blueprint(public_profile.public_bp)

    return app

__all__ = ['db']

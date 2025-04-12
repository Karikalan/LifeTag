from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    from app.routes import auth_routes
    from app.routes import basic_info_routes
    from app.routes import secured_info_routes  # (You'll add this soon)
    app.register_blueprint(auth_routes.bp)
    app.register_blueprint(basic_info_routes.bp)
    app.register_blueprint(secured_info_routes.bp)
    

    return app

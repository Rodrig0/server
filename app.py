import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_smorest import Api

from dotenv import load_dotenv

import models

from db import db
from resources.book import blp as BookBlueprint

load_dotenv("./.flaskenv")

def create_app(db_url=None):
    app = Flask(__name__)
    app.config.from_object(__name__)
    
    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})
    
    # sanity check route
    @app.route('/ping', methods=['GET'])
    def ping_pong():
        return jsonify('pong!')
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "API de Loja de roupas"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
        
    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(BookBlueprint)
    
    return app

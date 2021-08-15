from flask import Flask
from .extensions import (
    db, bcrypt_, migrate
)
from config import config_

# app factory (function that helps to create a flask app
# instance )

def create_app(config_name: str):
    app = Flask(__name__)

    # add config
    app.config.from_object(config_[config_name])

    # extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt_.init_app(app)

    # blueprints

    return app
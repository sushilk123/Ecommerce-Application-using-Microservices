# application/__init__.py
import config
import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager() #This object is used to hold the settings used for logging in.

def create_app():
    app = Flask(__name__)
    environment_configuration = os.environ['CONFIGURATION_SETUP']
    app.config.from_object(environment_configuration) #all the configuration values will be loaded into the app.config dictionary.

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():                 #https://flask.palletsprojects.com/en/1.1.x/appcontext/
        # Register blueprints
        from .user_api import user_api_blueprint        #https://flask.palletsprojects.com/en/1.1.x/blueprints/
        app.register_blueprint(user_api_blueprint)
        return app

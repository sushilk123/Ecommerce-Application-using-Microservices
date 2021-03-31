# config.py
import os
from dotenv import load_dotenv #Reads the key,value pair from .env and adds them to environment variable. It is great of managing app settings during development and in production using 12-factor principles.

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

class Config:
    SECRET_KEY = "F_7y2rITY34y0Am_5dCENg" #used to encrypt session cookies
    SQLALCHEMY_TRACK_MODIFICATIONS = False #To turn off flask sqlalchemy event system
    '''
    SQLALCHEMY_TRACK_MODIFICATIONS: If set to True (the default) Flask-SQLAlchemy will track modifications of objects and emit signals. 
    This requires extra memory and can be disabled if not needed.
    '''

class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///user_dev.db'
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    ENV = "production"
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///user_prod.db'
    SQLALCHEMY_ECHO = False


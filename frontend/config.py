# config.py
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Config:
    SECRET_KEY = 'PfwhOlKJ_3gvtiJCFD7l8HPJ9UW7A7tHWhOVat9SYPM'
    WTF_CSRF_SECRET_KEY = 'XdHPne39P4iRAJThcLv7Carq1DtKAkASZyO1Le4d_sE'


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True


class ProductionConfig(Config):
    ENV = "production"
    DEBUG = False


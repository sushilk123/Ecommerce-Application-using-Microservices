# run.py
from application import create_app, db
from application import models
from flask_migrate import Migrate  #https://flask-migrate.readthedocs.io/en/latest/

app = create_app()
migrate = Migrate(app, db)

"""
Flask-Migrate is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic. 
The database operations are made available through the Flask command-line interface or through the Flask-Script extension.
"""

#Line 16-33 : Disabling Session Cookie for APIs =>  https://flask-login.readthedocs.io/en/latest/

from flask import g
from flask.sessions import SecureCookieSessionInterface
from flask_login import user_loaded_from_header

class CustomSessionInterface(SecureCookieSessionInterface):
    """Prevent creating session from API requests."""

    def save_session(self, *args, **kwargs):
        if g.get('login_via_header'):
            return
        return super(CustomSessionInterface, self).save_session(*args,
                                                                **kwargs)

app.session_interface = CustomSessionInterface()

@user_loaded_from_header.connect
def user_loaded_from_header(self, user=None):
    g.login_via_header = True


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

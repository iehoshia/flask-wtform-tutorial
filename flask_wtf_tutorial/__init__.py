"""Initialize app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    app.config['RECAPTCHA_PUBLIC_KEY'] = 'iubhiukfgjbkhfvgkdfm'
    app.config['RECAPTCHA_PARAMETERS'] = {'size': '100%'}
    db = SQLAlchemy(app)
	migrate = Migrate(app, db)

    with app.app_context():
        # Import parts of our application
        from . import routes, models

        return app

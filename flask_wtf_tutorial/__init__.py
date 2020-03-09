"""Initialize app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    app.config['RECAPTCHA_PUBLIC_KEY'] = 'iubhiukfgjbkhfvgkdfm'
    app.config['RECAPTCHA_PARAMETERS'] = {'size': '100%'}

    with app.app_context():

        db.init_app(app)
        migrate.init_app(app,db)
        return app
    #return app

from flask_wtf_tutorial import routes, models
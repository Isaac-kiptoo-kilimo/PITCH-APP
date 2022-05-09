
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap=Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app=Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = '@@#243DD34gFAFDc_fjk3'

    # initializing the flask extensions
    # db = SQLAlchemy()
    # db.create_all()
    db.init_app(app)
    # login_manager = LoginManager(app)
    # login_manager.init_app(app)
    bootstrap.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
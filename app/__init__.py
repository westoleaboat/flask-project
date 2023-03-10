from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail, Message
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
# from app.models import Role #, User
from config import config
from flask_login import LoginManager
import os
from flask_jwt_extended import JWTManager
from flask_pagedown import PageDown
from dotenv import load_dotenv

# from ..config import ProductionConfig

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
jwt = JWTManager()
pagedown = PageDown()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app(config_name='production', db_url=None):
    app = Flask(__name__)
    load_dotenv()
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    jwt.init_app(app)
    pagedown.init_app(app)
    # create or update user roles
    # Role.insert_roles()

    # ensure all users are following themselves
    # User.add_self_follows()

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    return app


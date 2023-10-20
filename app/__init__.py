from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_moment import Moment
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
bootstrap = Bootstrap()
login = LoginManager()
login.login_view = "auth.login"
moment = Moment()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.static_folder = Config.STATIC_FOLDER
    app.template_folder = Config.TEMPLATES_FOLDER

    db.init_app(app)
    login.init_app(app)
    moment.init_app(app)
    bootstrap.init_app(app)

    # blueprint registration
    from app.Controller.errors import errors_blueprint as errors

    app.register_blueprint(errors)
    from app.Controller.auth_routes import auth_blueprint as auth

    app.register_blueprint(auth)
    from app.Controller.routes import routes_blueprint as routes

    app.register_blueprint(routes)

    return app

from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    app.config['SECRET_KEY'] = config[config_name].SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    

    db.init_app(app)

    # This is the main Blueprint
    from .main.views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # blueprint for auth routes in our app
    from .auth.views import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app

from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    app.config['SECRET_KEY'] = config[config_name].SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = config[config_name].SQLALCHEMY_DATABASE_URI
    

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models.auth_models import User
    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))
    

    # This is the main Blueprint
    from .main.views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # blueprint for auth routes in our app
    from .auth.views import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from .forms import AddAnimeForm, AddGameForm
from datetime import timedelta
from flask_babel import Babel

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    babel = Babel(app)

    login_manager.init_app(app)

    from app.config import SQLALCHEMY_DATABASE_URI, SECRET_KEY, UPLOAD_FOLDER
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=45)

    db.init_app(app)

    import app.routes as routes
    app.register_blueprint(routes.main_bp)
    app.register_blueprint(routes.anime_bp)
    app.register_blueprint(routes.note_bp)
    app.register_blueprint(routes.game_bp)
    app.register_blueprint(routes.emulators_bp)

    return app

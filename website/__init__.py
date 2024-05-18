from os import path

from flask import Flask
from .auth import auth
from .views import views
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

from .models import User, Note


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'tydfghjklkdtyfgjhkl dxtfcghvjkl'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    with app.app_context():
        db.create_all()

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

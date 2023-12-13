from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = '2016XXLFREESTYLE'
  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
  db.init_app(app)

  from .models import User, Note

  from .views import views
  from .auth import auth

  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/') ##you can define the prefix of the url the view needs to be accessed by for example if i had /auth/ i would have to nav to /auth/<route>

  with app.app_context():
    create_database(app)


  return app

def create_database(app):
  if not path.exists('website/' + DB_NAME):
    with app.app_context():
     db.create_all()
    print('Created Database!')
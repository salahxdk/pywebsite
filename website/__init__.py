from flask import Flask

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = '2016XXLFREESTYLE'
  
  from .views import views
  from .auth import auth

  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/') ##you can define the prefix of the url the view needs to be accessed by for example if i had /auth/ i would have to nav to /auth/<route>

  return app

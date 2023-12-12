from flask import Blueprint
###Blueprints are where you define the routes for your app
auth = Blueprint('auth', __name__) ##define blueprint

@auth.route('/login')
def login():
  return "<p>Login</p>"
@auth.route('/logout')
def logout():
  return "<p>Logout</p>"

@auth.route('/signup')
def sign_up():
  return "<p>Sign Up</p>"
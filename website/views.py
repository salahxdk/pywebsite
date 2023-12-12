from flask import Blueprint, render_template
###Blueprints are where you define the routes for your app

##Blueprints need to be registered in __init__.py
views = Blueprint('views', __name__) ##define blueprint

@views.route('/')
def home():
  return render_template('home.html') 
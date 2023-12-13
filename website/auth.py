from flask import Blueprint, render_template, request, flash, redirect, url_for
###Blueprints are where you define the routes for your app
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user




auth = Blueprint('auth', __name__) ##define blueprint

@auth.route('/')
def home():
  return render_template('home.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if user:
      if check_password_hash(user.password, password):
        flash('Logged in successfully!', category='success')
        login_user(user, remember=True) #logs the user in
        return redirect(url_for('views.home'))
      else:
        flash('Incorrect password', category='error')
  return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required #makes sure you can only access this route if you are logged in
def logout():
  logout_user()
  return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
  if request.method == 'POST':
    email = request.form.get('email') #calls the information from the form into the email variable, .get('<key>)
    first_name = request.form.get('firstName')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    user = User.query.filter_by(email=email).first()
    
    if user:
      flash('User already exists', category='error')
    if len(email) < 4:
      flash('Email must be greater than 3 characters.', category='error')
    elif len(first_name) < 2:
      flash('First name must be greater than 1 character.', category='error')
    elif password1 != password2:
      flash('Passwords don\'t match.', category='error')
    elif len(password1) < 7:
      flash('Password must be at least 7 characters.', category='error')
    else:
      try:
        #add user to db
        user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='scrypt'))
        db.session.add(user) ##adds the new user to the database
        db.session.commit() #commits the changes     
        login_user(user, remember=True) #logs the user in
        flash('Account created!', category='success')
        return redirect(url_for('views.home'))
      except Exception as e:
        flash('Email already in use', category='error')
  return render_template("signup.html", user=current_user)


from . import db
from flask_login import UserMixin #customclass that inherits from flask-login
from sqlalchemy.sql import func #allows for use of func.now() in line 8

class Note(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  data = db.Column(db.String(100000))
  date = db.Column(db.DateTime(timezone=True), default=func.now())
  user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #looks for a model called user in the schema and pulls the ID from that field, stored notes are attached to specific users

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True) #primary_key is the unique identifier for the key
  email = db.Column(db.String(150), unique=True) #unique,  no 2 users can have the same email
  password = db.Column(db.String(150))
  first_name = db.Column(db.String(150))
  notes = db.relationship('Note')
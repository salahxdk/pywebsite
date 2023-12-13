from flask import Blueprint, render_template, flash, request
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
###Blueprints are where you define the routes for your app

##Blueprints need to be registered in __init__.py
views = Blueprint('views', __name__) ##define blueprint

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
  if request.method == 'POST':
    note = request.form.get('note')

    if len(note) < 1:
      flash('Note is too short', category='error')
    else:
      new_note = Note(data=note, user_id=current_user.id) #passes the note data to the note variable and the current users id to the note
      db.session.add(new_note) #adds new note to DB
      db.session.commit()
      flash('Note added', category='success')

  return render_template('home.html', user=current_user) #passes current user to home page

@views.route('/delete-note', methods=['POST'])
def delete_note():
  note = json.loads(request.data)
  noteId = note['noteId']
  note = Note.query.get(noteId)
  if note:
    if note.user_id == current_user.id:
      db.session.delete(note)
      db.session.commit()
  return jsonify({})
from flask import render_template, request
import json

from app import app
from models import db, create_db, User

@app.route('/')
def index():
    create_db()
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/add_user')
def add_user():
    name = request.values.get('name')
    email = request.values.get('email')
    user = User(name, email)
    db.session.add(user)
    db.session.commit()
    return 'User added'

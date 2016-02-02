# -*- coding: utf-8 -*-

from flask import Flask
from constants import DatabaseConstants
from models import db

# start Flask app
#
app = Flask(__name__)

# configure database
#
app.config['SQLALCHEMY_DATABASE_URI'] = DatabaseConstants.DATABASE_URI
db.init_app(app)

from app import views

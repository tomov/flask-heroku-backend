from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

def get_datetime():
    return datetime.utcnow()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# should come from environment variables to ensure real security
app.config['SECRET_KEY'] = 'fweiujfbweiubvfeiw'

# path to sqlite database
# need to run the following in the python3 terminal window
# 'from app import db'
# db.create_all()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

# get an instance of the database
db = SQLAlchemy(app)

#First database entry was created manually in python3 terminal:
# from models import Task
# from datetime import datetime
# t = Task(title="First", date=datetime.utcnow())
# t
# db.session.add(t)
# db.session.commit()
# tasks = Task.query.all()
# tasks


# import everything from routes (needs to be after the app is instantiated)
from routes import *

if __name__ == '__main__':
    app.run(debug=True)
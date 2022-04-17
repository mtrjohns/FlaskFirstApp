# Data models file for the database
from asyncio import format_helpers
from app import db

class Task(db.Model):
     # Set columns required in the database
    
    # Set primary key
    id = db.Column(db.Integer, primary_key=True)
    # length of string () and cannot be empty nullable=False
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    
    # Function to represent each instance of this data model
    def __repr__(self):
        return f'{self.title} created on {self.date}'
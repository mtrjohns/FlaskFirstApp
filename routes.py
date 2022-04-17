#import current instance
from app import app
from flask import render_template

import forms

# Routes
@app.route('/')
def index():
    return render_template('index.html', current_title='Custom Title')

@app.route('/about')
def about():
    form = forms.AddTaskForm()
    return render_template('about.html', form=form)

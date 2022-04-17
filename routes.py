#import current instance
from app import app, db
from flask import render_template, redirect, url_for
from models import Task
from datetime import datetime

import forms

# Routes
@app.route('/')
def index():
    # create a list of tasks
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = forms.AddTaskForm()
    # validate the information returns true
    if form.validate_on_submit():
        # get task entered by user
        t = Task(title=form.title.data, date=datetime.utcnow())
        # add and commit to database
        db.session.add(t)
        db.session.commit()     
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

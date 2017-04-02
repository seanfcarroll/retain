#!/usr/bin/env python

from flask import Flask, flash, redirect, url_for
from flask import request
from flask import render_template

from project import config
from project.models import *
from project.controllers import hello

app = Flask(__name__)
app.secret_key = 'some_secret'

# All views below
@app.route("/",  methods=['GET', 'POST'])
def index():
    form = ConceptSubmissionForm(request.form)
    if request.method == 'POST' and form.validate():
    	print "hi"
        # user = User(form.concept.data, form.R_score.data, form.C_score.data)
        # db_session.add(user)
        flash('Successfully submitted.')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

@app.route("/add",  methods=['GET', 'POST'])
def add():
	print "hi"
	form = AddConceptSubmissionForm(request.form)
	if request.method == 'POST' and form.validate():
		print "reached"
		# user = User(form.concept.data, form.R_score.data, form.C_score.data)
		# db_session.add(user)
		flash('Successfully submitted.')
		return redirect(url_for('add'))
	return render_template('add-concept.html', form=form)

@app.route("/fluid")
def fluid():
    return render_template('fluid.html')

@app.route("/hero")
def hero():
    return render_template('hero.html')

@app.route("/layout")
def layout():
    return render_template('layout-template.html')


# Error Pages
@app.errorhandler(500)
def error_page(e):
    return render_template('error_pages/500.html'), 500

@app.errorhandler(404)
def not_found(e):
    return render_template('error_pages/404.html'), 404

# Lazy Views
app.add_url_rule('/hello', view_func=hello.hello_world)



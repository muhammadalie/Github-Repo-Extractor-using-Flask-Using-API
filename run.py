#!flask/bin/python
import sqlite3
from flask import Flask
from flask.ext.login import LoginManager
app= Flask(__name__)
app.config.from_object('config')
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required,user_logged_in
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField,PasswordField, validators,TextField,TextAreaField,IntegerField
from wtforms.validators import DataRequired
import requests
import json
class URLForm(Form):
	url = StringField('url', validators=[DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def home():
	form= URLForm()
	if form.validate_on_submit():
		name=form.url.data
		url='https://api.github.com/users/'+name+'/repos'
		r=requests.get(url)
		a=r.text
		repos=json.loads(a)
				 	 		
	return render_template('home.html',form=form,r=repos)

app.run(debug=True)

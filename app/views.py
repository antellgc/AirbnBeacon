from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
import sqlite3
import pandas as pd

database_path = './airbnb.db'

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Greg'}  # fake user
    posts = [  # fake array of posts
	    { 
	        'author': {'nickname': 'John'}, 
	        'body': 'Beautiful day in Portland!' 
	    },
	    { 
	        'author': {'nickname': 'Susan'}, 
	        'body': 'The Avengers movie was so cool!' 
	    }
	]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID="%s", remember_me=%s' %
			(form.openid.data, str(form.remember_me.data)))
		return redirect('/index')
	return render_template('login.html',
		title='Sign In',
		form=form)

@app.route('/db')
def get_db():
	conn = sqlite3.connect(database_path)
	query = conn.execute("select * from properties")
	cols = [column[0] for column in query.description]
	results = query.fetchall()
	results_df = pd.DataFrame(results, columns=cols)

	lines = []
	for i in range(0,10):
		lines.append(results_df.iloc[i]['price'])
	return render_template("db.html",
    	title='Database',
    	lines=lines)

@app.route('/theme')
def get_started():
	return render_template("theme.html")

@app.route('/input')
def get_input():
	return render_template("input.html",
		title='Input')

@app.route('/map')
def get_map():
	return render_template("map.html",
		title='Map')

@app.route('/about')
def get_about():
	return render_template("about.html",
		title='About')

from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
import sqlite3
import pandas as pd
import gmaps
import gmplot

database_path = './airbnb.db'

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                           title='Home')

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

@app.route('/map', methods=['GET', 'POST'])
def get_map():
	return render_template("map.html",
		title='Map')

@app.route('/about')
def get_about():
	return render_template("about.html",
		title='About')

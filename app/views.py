from flask import render_template, flash, request
from app import app
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

@app.route('/altview')
def altview():
    return render_template("altview.html",
                           title='Alt')

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

@app.route('/explore')
def get_input():
    return render_template("explore.html",
        title='Explore')

@app.route('/explore/info', methods=['POST'])
def get_property_info():
    address = request.form['address']
    accommodates = request.form['accommodates']
    property_type = request.form['property_type']
    room_type = request.form['room_type']
    bedrooms=request.form['bedrooms']
    bathrooms=request.form['bathrooms']
    price = request.form['price']
    return render_template("info.html", title='Input',
		address=address, accommodates=accommodates,
		property_type=property_type, room_type=room_type,
		bedrooms=bedrooms, bathrooms=bathrooms, price=price)

@app.route('/map', methods=['GET', 'POST'])
def get_map():
	return render_template("map.html",
		title='Map')

@app.route('/about')
def get_about():
	return render_template("about.html",
		title='About')

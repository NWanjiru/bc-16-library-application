from flask import render_template

from app import app

@app.route('/')
def signup():

	return (render_template("signup.html"))

@app.route('/login')
def login():

	return (render_template("login.html"))

@app.route('/signup')
def signup2():

	return (render_template("signup.html"))
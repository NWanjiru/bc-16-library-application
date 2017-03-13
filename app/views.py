from flask import render_template

from app import app

@app.route('/')
def signup():

	return (render_template("signup.html"))
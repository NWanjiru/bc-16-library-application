from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy 
from library.models import db, User

import os

app = Flask(__name__)
import views

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config ['DEBUG'] = True
db.app=app
db.init_app(app)
db.create_all()

@app.route('/signup',methods=['GET','POST'])
def signup():
	if request.method=='POST':
		username = request.form['username']
		email = request.form['email']
		password = request.form['password']
		user = User(username, email,password)
		db.session.add(user)
		db.session.commit()
		return(render_template("login.html"))

	else:
		return(render_template("signup.html"))

@app.route('/login',methods=['GET','POST'])
@app.route('/',methods=['GET','POST'])
def login():
	if request.method=='POST':
		username = request.form['username']
		password = request.form['password']
		user = User.query.filter_by(username=username).first()
		if user is not None:
			if password == user.password:
				return("Login Successful")
			else:
				return("Wrong Password")

	else:

		return(render_template("login.html"))
	

if __name__ == '__main__':
	
	app.run()

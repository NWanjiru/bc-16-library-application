from flask import Flask, flash, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy 
from flask_login import login_required, login_user, logout_user, LoginManager
from library.models import db, User, Books
import jinja2

import os

app = Flask(__name__)
app.secret_key = 'cray one'

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config ['DEBUG'] = True
db.app=app
db.init_app(app)
login_manager.init_app(app)
db.create_all()


@app.route('/signup',methods=['GET','POST'])
def signup():
	if request.method=='POST':
		username = request.form['username']
		email = request.form['email']
		password = request.form['password']
		user_username = User.query.filter_by(username=username).first()
		if user_username:
			return('That username is already in use')
		user_email = User.query.filter_by(email=email).first()
		if user_email:
			return('That email address already exists in the system.')
		else:
			user = User(username, email,password)
			db.session.add(user)
			db.session.commit()
			return(redirect(url_for("login")))

	else:
		return(render_template("signup.html"))

@app.route('/login',methods=['GET','POST'])
@app.route('/', methods=['GET'])

def login():
	""" Check if username or password exist and if user is admin"""

	if request.method=='POST':
		username = request.form['username']
		password = request.form['password']
		user = User.query.filter_by(username=username).first()

		if user:
			if username == 'admin' and password == 'cray one':
				login_user(user)

				return(redirect(url_for("view_books")))

		if password == user.password:
			login_user(user)
			return(redirect(url_for("view_books")))

		else:
			return("Wrong Password")

	else:
		return(render_template('login.html'))

@app.route('/logout')
def logout():
	logout_user()
	return(redirect(url_for("login")))

@app.route('/books',methods=['GET'])
def add_book():
	
	if request.method=='POST':
		name = request.form['name']
		author = request.form['author']
		category = request.form['category']
		book = Books(name, author, category)
		db.session.add(book)
		db.session.commit()
	return(render_template('books.html'))
		


@app.route('/view', methods=['GET'])
def view_books():
	return (render_template('view.html', books = Books.query.all()))




if __name__ == '__main__':
	
	app.run()

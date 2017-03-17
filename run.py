from flask import Flask, flash, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy 
from flask_login import login_required, login_user, logout_user, LoginManager
from library.models import db, User, Books
#import Flask-WTF 
import jinja2

import os

app = Flask(__name__)
app.secret_key = 'cray one'


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config ['DEBUG'] = True

db.app=app
db.init_app(app)
db.create_all()

# login_manager = LoginManager()
# login_manager.init_app(app)


@app.route('/signup',methods=['GET','POST'])
def signup():
	""" Check what method has called the function. """
	# If the method is POST, 
	# query the database for 'username' and 'email' matches'. 
	# Add new user and their details into the database, if the entries are unique."""


	if request.method=='POST':
		username = request.form['username']
		email = request.form['email']
		password = request.form['password']
		user_username = User.query.filter_by(username=username).first()
		if user_username:
			flash('That username is already in use')
		user_email = User.query.filter_by(email=email).first()
		if user_email:
			flash('That email address already exists in the system.')
		else:
			user = User(username, email,password)
			db.session.add(user)
			db.session.commit()
			flash(redirect(url_for("login")))

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
				login_user(user, remember=True)
				# """Login and check whether the user credentials match the set admin credentials """

				return(redirect(url_for("view_books")))

			if password == user.password:
				login_user(user, remember=True)
				# """ Check whether login password matches the stored password for an already registered user"""

				return(redirect(url_for("view_books")))

			else:
				return("Wrong Password")
		else:
			return('User does not exist!')

	else:
		return(render_template('login.html'))

# @app.route('/logout')
# #@login_required
# def logout():

# 	""" Allows user to end the current session """

# 	logout_user()
# 	return(redirect(url_for("login")))

@app.route('/books',methods=['GET', 'POST'])
#@login_required
def add_book():
	""" Check which method has called the function and add new book""" 
	# if the calling method is 'POST'
	# else, display the list of books that already exist in the database"""

	if request.method=='POST':
		name = request.form['name']
		author = request.form['author']
		category = request.form['category']
		book = Books(name, author, category)
		db.session.add(book)
		db.session.commit()
		return(redirect(url_for('view_books')))
	else:
		return(render_template("books.html"))
		


@app.route('/view', methods=['GET'])
#@login_required
def view_books():
	""" Query the database for all entries in the Books table and display them in the specified template """

	return (render_template('view.html', books = Books.query.all()))




if __name__ == '__main__':
	app.run()

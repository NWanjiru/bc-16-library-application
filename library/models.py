from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
#from run import login_manager
db = SQLAlchemy()

class User(db.Model):

	__tablename__ = 'user'

	id = Column(Integer, primary_key = True)
	username = Column(String(50), unique=True, nullable = False)
	email = Column(String(80), unique=True, nullable = True)
	password = Column(String(80), nullable = False)
	admin = Column(Boolean, default=False) 
	is_active =Column(Boolean, default=False)

	def __init__(self, username, email, password, admin = False):
		self.username = username
		self.email = email
		self.password = password
		self.admin = admin

	def __repr__(self):
		return('<User %r>' % self.id)

# @login_manager.user_loader

# def load_user(user_id):

#     return Users.query.get(int(user_id))

class Books(db.Model):

	__tablename__ = 'book'

	id = Column(Integer, primary_key = True)
	name = Column(String(120), nullable = False)
	author = Column(String(120), nullable = False)
	category = Column(String(120), nullable = True)
	available = Column(Integer)
	user_id = Column(Integer, ForeignKey('user.id'))
	#user = relationship(User)

	def __init__(self, name, author, category, available = True):
		self.name = name
		self.author = author
		self.category = category
		self.available = available

	def __repr__(self):
		return('<Books %r>' % self.id)
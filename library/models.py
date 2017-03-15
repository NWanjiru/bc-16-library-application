from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

db = SQLAlchemy()

class User(db.Model):

	__tablename__ = 'user'

	id = Column(Integer, primary_key = True)
	username = Column(String(50), unique=True, nullable = False)
	email = Column(String(80), unique=True, nullable = True)
	password = Column(String(80), nullable = False)
	admin = Column(Boolean, default=False) 

	def __init__(self, username, email, password, admin = False):
		self.username = username
		self.email = email
		self.password = password
		self.admin = admin


class Books(db.Model):

	__tablename__ = 'books'

	id = Column(Integer, primary_key = True)
	name = Column(String(120), nullable = False)
	Author = Column(String(120), nullable = False)
	category = Column(String(120), nullable = True)
	available = Column(Boolean, default = True)
	user_id = Column(Integer, ForeignKey('user.id'))
	#user = relationship(User)

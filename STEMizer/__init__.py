import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from STEMizer import main_functions
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '30aea3f479006422c7fd8d81b144e0ab'

#setting up the database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

'''An instance of SQLAlchemy, represented as classes like in object-oriented paradigm, also known as models'''
db = SQLAlchemy(app)

'''An instance of Bcrypt'''
bcrypt = Bcrypt(app)

'''An instance of LoginManager'''
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

'''Issue with self looping'''
from STEMizer import routes
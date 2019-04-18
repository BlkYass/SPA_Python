#Module to intialize the application and bring together different components

from flask import Flask  #import the Flask class
from flask_sqlalchemy import SQLAlchemy  #import flask sqlAlchemy extention
from flask_bcrypt import Bcrypt          #import flask bcrypt extention for password hasging
from flask_login import LoginManager  #LoginManager class contains the code that lets the application and Flask-Login work together, such as how to load a user from an ID, where to send users when they need to log in, and the like.
import os
#the package app is defined by the app directory and the __init__.py module  
#and is referenced in the 'from app import routes' below
#The app variable is defined as an instance of class Flask in the __init__.py module
#which makes it a member of the app package.
#here we are creating our flask application
app = Flask(__name__) #__name__ is the name of the current Python module

if os.environ.get('ENV') == 'PRODUCTION':
    app.config['DEBUG'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

else:
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True #To turn off the Flask-SQLAlchemy event system in order not to waste system resources 
    app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245' #Setting up simple configuration for now
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Places.db' #Configuring a database named Places.db located in the main directory of the application 

db = SQLAlchemy(app)   #initalize app with database

bcrypt = Bcrypt(app)   #initalize app with passowrd hashing

login_manager = LoginManager(app)   #initalize app with Login manager
login_manager.login_view = 'login'  #set The name of the log in view 
login_manager.login_message_category = 'info'  #customize the message category flashed when a user attempts to access a login_required view without being logged in


from app import routes    #in order to fix circular import we import routes module after instantiation of the app variable

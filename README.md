# Introduction

implementing an app that lists shops nearby the location of the user.this application is still under devlopement.

tools used:
visual studio code 
git bach

I will be using Flask a lightweight Python framework for web applications.

Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions. And before you ask: It's BSD licensed! http://flask.pocoo.org/

Flask provides the basics for URL routing and page rendering also it doesn't directly provide features like form validation, database abstraction, authentication, and so on. Such features are instead provided by special Python packages called Flask extensions like flask-sqlalchemy Flask-Login descripton of used extensions can be found bellow. 

Python comes with built-in support for SQLite.SQLite is convenient because it doesn’t require setting up a separate database server and is built-in to Python. However, if concurrent requests try to write to the database at the same time,they will slow down as each write happens sequentially. Small applications won’t notice this. Once the app become big switching to a different database like mysql will more conviniant.
While lightweight and easy to use, Flask’s built-in server is not suitable for production as it doesn’t scale well. Some of the options available for properly running Flask in production are documented here http://flask.pocoo.org/docs/1.0/deploying/#deployment.

I am using a google place api key. please make sure to have a valid google api key to make request and restricted to your IP adresse or use one without restriction.

## Requirements
```bash
install Python 3.6.5
install pipenv using pip install pipenv
update pip 18.1
google places api key https://developers.google.com/places/web-service/get-api-key
```
## Quickstart

```bash
$ # Clone the respository, and cd to it
$ git clone https://github.com/issambni/SPA_Python.git

$ # Creating a virtualenv for this project using
$ pipenv --python python3 or (replace python3 with the path to the executable installed python)
$ #Activate the virtual environment using
$ pipenv shell

$ # Run the Flask application on windows
$ set FLASK_APP=run.py
$ # Run the Flask application on Mac/linux
$ import FLASK_APP=run.py
$ flask run
```
## Content of the application

The directory structure should look as follows:
```bash
.SPA_Python            # root directory 
├── app                  # package that host the application
|     ├── static #css and javascript
|     |          ├── main.css
|     |          ├── sample_photos
|     |          ├── Phptos
|     |          ├──localization-icon.png
|     ├── templates    # views directory
|     |          ├── index.html              #entry page  
|     |          ├── login.html              #page for user to login
|     |          ├── register.html           #page for user to register
|     |          ├── NearbyShops.html        #page to display shops near user lication
|     |          ├── pref_Shops.html         #page to dispkay like places
|     ├──Places.db    #database file
|     ├──__init__.py  #module to configure and intialize the flask application
|     ├──forms.py     #module for form models for login and registration
|     ├──models.py    #module for database classes
|     ├──routes.py    #module for handling views 
├── pipfile             # file with dependencies and flask extention
├── pipfile.lock        #
├── run.py              # main module to run the application
├── README.md           #Information about the app

```
## Description of used packages,Modules and flask extensions 

```bash
-pipfile contains installed packages:
flask 
 lightweight WSGI web application framework
requests 
flask-sqlalchemy 
 Adds SQLAlchemy support to the Flask application
flask-wtf
 Simple integration of Flask and WTForms it handles passing form data to the form
flask-login 
 provides user session management for Flask. It handles the common tasks of logging in, logging out, and remembering your users’ sessions.
flask-bootstrap
bcrypt 
 password hashing
sqlalchemy 
 The Python SQL Toolkit and Object Relational Mapper    
flask-bcrypt 
password hashing for flask
 geocoder Simple and consistent geocoding library written in Python

-pipfile.lock 
contains The details of the environment (all installed packages with pinned versions and other details) 
This file was automatically generated and will be automatically updated upon installing new packages and should not be modified by the user.
```









## Quick Intro
```bash
used language and framework

Python 3.6.5
pip 18.1
Flask 
google places api
sqlite 
postgresql

```

## Content of the application

The directory structure should look as follows:
```bash
.SPA_Python            # root directory 
├── app                  # package that host the application
|     ├── static #css and javascript
|     |          ├── main.css
|     |          ├── sample_photos
|     |          ├── Photos
|     |          ├──localization-icon.png
|     ├── templates    # views directory
|     |          ├── index.html              #entry page  
|     |          ├── login.html              #page for user to login
|     |          ├── register.html           #page for user to register
|     |          ├── NearbyShops.html        #page to display shops near user location
|     |          ├── pref_Shops.html         #page to dispkay like places
|     ├──Places.db    #database file
|     ├──__init__.py  #module to configure and intialize the flask application
|     ├──forms.py     #module for form models for login and registration
|     ├──models.py    #module for database classes
|     ├──routes.py    #module for handling views 
├── requirement.txt    # file with dependencies and flask extention
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


```








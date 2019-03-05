#Module for handling routes logic
#render_template flask function returns the passed html page or templates from the template directory
#url_for flask function used to build a url for a specific function also used in templates passing it to href with route as parametre
from flask import render_template, url_for, flash, redirect, request, jsonify, send_from_directory
from app import app, db, bcrypt  #importing app varialble with db and bcrybt components
from .forms import RegistrationForm, LoginForm  #importing registration and login classes from forms module
from .models import User, pref_place  #inmporting database models         
from flask_login import login_user, current_user, logout_user, login_required
import urllib.parse #module defines a standard interface to break URL strings up in components
import requests     #module for making requests to the google api
import geocoder     #geocoding library to get user location
import json         #buit-in package to work with JSON data
import imghdr       #module to determine type of an image contained in a file or byte stream
import io           #module for handling files
import os           #module provides a portable way of using operating system dependent functionality

#url's for making the requests to the google places api
nearby_search_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
photos_url = "https://maps.googleapis.com/maps/api/place/photo?"

#index route
@app.route("/")
@app.route('/index')
def index():
    #display sample photos
    sample_image_name = os.listdir('App/static/sample_photos')

    return render_template('index.html',sample_image_name=sample_image_name)

#register route
@app.route('/register', methods=['GET', 'POST'])
def register():    
    form = RegistrationForm()
    if form.validate_on_submit():
        #hashing the password
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(email=form.email.data, password=hashed_password) 
        db.session.add(user) #adding the user to the database 
        db.session.commit()  #saving to the database
                
        flash(f'Account created for {form.email.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

#login route
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        #check if user exists and password are valid
        if user and bcrypt.check_password_hash(user.password, form.password.data): 
            login_user(user, remember=form.remember.data) 
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('NearbyShops'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

#route for generating nearby places
@app.route("/NearbyShops")
@login_required
def NearbyShops():
    
    g = geocoder.ip('me') #return information about user location
    ln = g.json #converting the response to json format
    loc = str(float(ln['lat']))+","+str(float(ln['lng'])) #extract latitude and logitude from json ln
    
    #combine the neaby search url with parameters using urllib.parse.urlencode functioin to convert to text
    final_url = nearby_search_url + urllib.parse.urlencode({'location':loc,
                                                            'radius':'1500',
                                                            'type':'restaurant,beauty_salon,pet_store,car_wash,cafe,home_goods_store,veterinary_care,supermarket,store',
                                                            'key':'AIzaSyD_bvbG9mgu59qr31u4YA2b2TYoIh76ovc'})
    #making the request to the places api
    places_req = requests.get(final_url)
    
    #convert the response to text
    places_req.text
    #storing the response as json to the results variable
    results = json.loads(places_req.text)

    list_photo_reference = []   #list to store photo reference of each place in the results 
    list_name = []     #list to store the name of each place in the results 
    list_response_photo = []  #list to store the binary content of photos of each place in the results
    lent = len(results)
   
    #storing the photo reference of each place in a list
    for i in range(lent):
        for ph in results["results"][i]["photos"]:
            list_photo_reference.append(ph["photo_reference"])
    
    #storing the name of each place in a list
    for n in results["results"]:
       list_name.append(n["name"])
    
    #making the request to the photo places api for each photo reference
    for ref in list_photo_reference:
        photo_final_url = photos_url + urllib.parse.urlencode({'maxwidth' :'500', 
                                                               'photoreference' :ref,
                                                               'key':'AIzaSyD_bvbG9mgu59qr31u4YA2b2TYoIh76ovc'})                                                     
        photos_req = requests.get(photo_final_url)
        list_response_photo.append(photos_req.content)
    
    #writing the content of the list_response_photo list to files in photos folder
    for rq,name in zip(list_response_photo,list_name):
            photo_name= name.replace(" ","_") + "." + imghdr.what("", rq)
                
            photo_dir = "App/static/photos/" + photo_name
            
            with open(photo_dir, "wb+") as f:
                f.write(rq)
                
    
    #variable to display the photos on the template
    image_name = os.listdir('App/static/photos')
  
   
    return render_template('NearbyShops.html', title='Nearby Shops',image_name=image_name)
       
#route for selected liked shops
@app.route("/pref_Shops")
@login_required
def pref_Shops():
    
    return render_template('pref_Shops.html', title='My preferred Shops')  

#logout route
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

#404 error handeler route
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

#500 error handler route
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500



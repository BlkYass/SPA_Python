#Module for handling routes logic

from flask import render_template, url_for, flash, redirect, request, jsonify, send_from_directory
from app import app, db, bcrypt  #importing app varialble with db and bcrybt components
from .forms import RegistrationForm, LoginForm  #importing local modules
from .models import User, pref_place
from flask_login import login_user, current_user, logout_user, login_required
import urllib.parse
import requests
import geocoder
import json
import imghdr
import io
import os

#url's for making the requests to the google places api
nearby_search_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
photos_url = "https://maps.googleapis.com/maps/api/place/photo?"

#index route
@app.route("/")
@app.route('/index')
def index():
    sample_image_name = os.listdir('App/static/sample_photos')

    return render_template('index.html',sample_image_name=sample_image_name)

#register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    '''
    if current_user.is_authenticated:
        return redirect(url_for('NearbyShops'))
    '''    
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
    '''
    if current_user.is_authenticated: 
        return redirect(url_for('NearbyShops'))
    '''    
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
    
    g = geocoder.ip('me')
    ln = g.json
    loc = str(float(ln['lat']))+","+str(float(ln['lng']))
    
    final_url = nearby_search_url + urllib.parse.urlencode({'location':loc,
                                                            'radius':'2500',
                                                            'type':'restaurant',
                                                            'key':'AIzaSyBSb_FEkrkczt1ZV0aEHwZ_vzMtGgWFCDM'})
    places_req = requests.get(final_url)
    places_req.text
    results = json.loads(places_req.text)

    list_photo_reference = []
    list_name = []
    list_requests = []
    lent = len(results)
   
    
    for i in range(lent):
        for ph in results["results"][i]["photos"]:
            list_photo_reference.append(ph["photo_reference"])
    
    for n in results["results"]:
       list_name.append(n["name"])
    
    for ref in list_photo_reference:
        photo_final_url = photos_url + urllib.parse.urlencode({'maxwidth' :'500', 
                                                               'photoreference' :ref,
                                                               'key':'AIzaSyBSb_FEkrkczt1ZV0aEHwZ_vzMtGgWFCDM'})
        photos_req = requests.get(photo_final_url)
        list_requests.append(photos_req.content)
    
    
    for rq,name in zip(list_requests,list_name):
            photo_name= name.replace(" ","_") + "." + imghdr.what("", rq)
                
            photo_dir = "App/static/photos/" + photo_name
            
            with open(photo_dir, "wb+") as f:
                f.write(rq)
                
    
    
    image_name = os.listdir('App/static/photos')
  
   
    return render_template('NearbyShops.html', title='Nearby Shops',image_name=image_name)
       
#route for selected liked shops
@app.route("/pref_Shops")
@login_required
def pref_Shops():
    
    return render_template('pref_Shops.html', title='My preferred Shops')  

#logout route
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))



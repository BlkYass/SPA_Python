# Module for database models importing necessary modules
from app import db, login_manager  
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#initial model for users. fields can be updated 
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    pref_place = db.relationship('pref_place', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.email}', '{self.pref_place}')"

#intial model for liked places to be stored in database. fields can be updated   
class pref_place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date_like = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    ln = db.Column(db.Integer, nullable=False)
    lg = db.Column(db.Integer, nullable=False)
    image_file = db.Column(db.LargeBinary, nullable=False, default='default.jpg')
    user_id = db.Column(db.String(20), db.ForeignKey('user.email'), nullable=False)

    def __repr__(self):
        return f"pref_place('{self.name}')"

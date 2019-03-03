#module to store web form classes using flask-wtf extension using flask-wtf we can define the form fields and render them using an HTML template. It is also possible to apply validation to the WTF field.
from flask_wtf import FlaskForm #Without any configuration, the FlaskForm will be a session secure form with csrf (Cross-Site Request Forgery) protection
'''
    Flask-WTF provided its own wrappers around the WTForms fields and validators
    The four classes that represent the field types used for each form. For each field, 
    an object is created as a class variable in the LoginForm class. 
    Each field is given a description or label as a first argument.
    wtforms handles form validation using built-in or customized form validators.
    The optional validators argument used im most of the fields is used to attach 
    validation behaviors to fields. The DataRequired validator simply checks that the field 
    is not submitted empty.
'''
from wtforms import StringField, PasswordField, SubmitField, BooleanField 
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from .models import User

#registration class
class RegistrationForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    #function to check if email already exist 
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

#login class
class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

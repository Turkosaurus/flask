from flask_wtf import FlaskForm
from wtforms import StringField, passwordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email

class ResistrationForm(FlaskForm):
    username - StringField('Username', 
                        validators=[DataRequired(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()j])
    password = PasswordField('Password', 
                        validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username - StringField('Email', 
                        validators=[DataRequired(), Email()])
    email = StringField('Email',
                        validators=[DataRequired()])
    password = PasswordField('Password', 
                        validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
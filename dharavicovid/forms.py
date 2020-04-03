from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed ### file upload
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from dharavicovid.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    
    image_file = FileField('Upload Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    #bike_image = FileField('Upload a picture of bike', validators=[FileAllowed(['jpg', 'png'])])
    
    #bike_certificate = StringField('Bike Cetrtificate No.', validators=[DataRequired(), EqualTo('bike_certificate')])
    #certificate = BooleanField('Bike Certification')

    submit = SubmitField('Sign Up')
    # validation errors
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists. Please choose a different one')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email id already exists. Please choose a different one')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


'''

class ReportForm(FlaskForm):
    bikeid = StringField('bike_id',
                        validators=[DataRequired(), Email()])
    email = StringField('Email')
    submit = SubmitField('Submit')
'''
'''
class LocationQuery(FlaskForm):
    origin = StringField('Origin', validators=[])
    destination = StringField('Destination', validators=[])
    bike_data = [(1,2), (2, 4), (5, 6), (7, 8), (9, 10)]
    
    def distance(self):
        return ()



''' 
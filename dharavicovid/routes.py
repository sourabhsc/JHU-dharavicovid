
from flask import render_template, url_for, flash, redirect, request ### after user login 
from dharavicovid.models import User
from dharavicovid.forms import RegistrationForm, LoginForm
from dharavicovid import app, db, bcrypt

from flask_login import login_user, current_user, logout_user, login_required # for removign bars

import secrets
from PIL import Image

import os

posts = [
    {
        'author': 'Team 94',
        'title': 'DharaviCovid',
        'content': 'Social distancing is not feasible in dense settlements of developing countries. We propose that 10-15 families in a settlement strengthen together as a single unit. Unit-wise pool testing and isolation helps manage infection transmission, combined finances of the unit helps mitigate the financial stress for a single daily-wage family.'    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


'''
@app.route("/report", methods=['GET', 'POST'])
@login_required
def report():
    form = ReportForm()
    if current_user.is_authenticated:

        return redirect(url_for('home'))

    return render_template('report.html', title='Report', form = form)
'''

def save_picture(form_picture, folder):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/%s'%(folder), picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

def save_picture_bike(form_picture, folder):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/%s'%(folder), picture_fn)

    output_size = (250, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn





@app.route("/register", methods=['GET', 'POST']) ### allowing posing requests here to eneter
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        if form.image_file.data:
            picture_file = save_picture(form.image_file.data, 'profile_pics')
            current_user.image_file = picture_file
        if form.bike_image.data:

            bike_image_file = save_picture_bike(form.bike_image.data, 'bike_pics')
            current_user.bike_image = bike_image_file
        user = User(username=form.username.data, email=form.email.data, password=hashed_password, certificate=form.certificate.data, image_file=picture_file, bike_image=bike_image_file)

        db.session.add(user)
        db.session.commit()
        # what to do for same user logggin again
        flash('Your account created! You can now log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:

            flash('Login Unsuccessful. Please check email and password', 'danger')
    
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
##cahnge layout as well

@app.route("/account", methods= ["GET", "POST"])
@login_required
def account():

    #form = LocationQuery()
    image_file = url_for('static', filename='profile_pics/' +current_user.image_file) 
    #bike_image_file = url_for('static', filename='bike_pics/' +current_user.bike_image) 

    #if method == "POST":
    #    print ()

    return render_template('account.html', title='Account', image_file=image_file, sunny=True)#, bike_image=bike_image_file)


'''
@app.route("/account", methods= ["GET", "POST"])

def account():

    form = LocationQuery()
    image_file = url_for('static', filename='profile_pics/' +current_user.image_file) 
    bike_image_file = url_for('static', filename='bike_pics/' +current_user.bike_image) 



    return render_template('account.html', title='Account', image_file=image_file, bike_image=bike_image_file, form=form)


'''


'''
@app.route("/map")
def mapview():
    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )
    sndmap = Map(
        identifier="sndmap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
             'lat': 37.4419,
             'lng': -122.1419,
             'infobox': "<b>Hello World</b>"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
             'lat': 37.4300,
             'lng': -122.1400,
             'infobox': "<b>Hello World from other place</b>"
          }
        ]
    )
    return render_template('example.html', mymap=mymap, sndmap=sndmap)

'''


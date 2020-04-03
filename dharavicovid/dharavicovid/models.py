from datetime import datetime
from dharavicovid import db, login_manager ##managing login sessions
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

# is authenticated
# is anonymous
# is active
# get id
## all these methods are used 


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)##unique id
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    #bike_image = db.Column(db.String(20), nullable=False, default='default.png')
    #certificate = db.Column(db.Boolean, nullable=False, default=False)

    password = db.Column(db.String(60), nullable=True)
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"#,  '{self.certificate}', '{self.bike_image}')"
## set up db.relationship posts = db.relationship('Post', backref='author', lazy='True')
#

## modify login route now
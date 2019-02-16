from datetime import datetime
from flask_blog import db, login_manager
from flask_login import UserMixin # this is 4 things checked by logging manager, see flask_login documentation
import random

@login_manager.user_loader # This is to reload the user using user ID stored in session.
def load_user(user_id):
    return User.query.get(int(user_id)) # To LOGIN_MANAGER to know how to get the user ID


"""
in order to user user_loader extension, it needs, User model(class) is to be implemented in a way it needs.
as it needs, it needs user model to have specific methods to be implemented when creating user model.
those methods can be automatically implement by inheriting UserMixin
"""


class User(db.Model, UserMixin): # by inherinting required methods will come to this model
    id = db.Column(db.Integer, primary_key=True)
    username  = db.Column(db.String(20), unique=True, nullable=False) 
    email  = db.Column(db.String(120), unique=True, nullable=False) 
    image_file = db.Column(db.String(20), unique=False, nullable=False, default=f'default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True) # setting 1-m relationship, here post is all lowercase as Post moodel(Post Class) creates a table as post(lowercase) automatically, so we need to refer that post table, not Post model.

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title  = db.Column(db.String(100), nullable=False) 
    date_posted  = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # here we dont use () as we dont want to call the function, we just need to set as after we can call when outtung it to database
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # here in user.id, user is all lower case as User model(User class) create tabel user(all lower) automatically, so we need to refer id in that table user, not User model. 
                                                              # if want to set specific name for table, there's a specific TABLE?NAME attribute

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

from datetime import datetime
from flask_blog import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username  = db.Column(db.String(20), unique=True, nullable=False) 
    email  = db.Column(db.String(120), unique=True, nullable=False) 
    image_file = db.Column(db.String(20), unique=True, nullable=False, default='def.jpg')
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
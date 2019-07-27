from STEMizer import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id =db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    image_file = db.Column(db.String(20),nullable=False,default='default.jpg')
    password = db.Column(db.String(60),nullable=False)
    #posts attribute has a relationship to the Post model
    #backref is similar to adding another column to the Post model
    #with lazy we retrieve all posts from a user easily
    posts = db.relationship('Post',backref='author',lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    #the default is datetime without () because the function is the parameter not the actual value of
    # the function at the current time
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    content = db.Column(db.Text,nullable=False)
    #lower case user because its table name and column name
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"
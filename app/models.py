from .exts import db
from datetime import datetime,timezone
from flask_login import UserMixin
from .exts import login_manager

class TimestampMixin(object):
    created = db.Column(
        db.DateTime,nullable = False, default = datetime.now(timezone.utc)
    )
    updated = db.Column(db.DateTime,onupdate = datetime.now(timezone.utc))
    status = db.Column(db.Integer,default = 0)

class User(TimestampMixin,UserMixin,db.Model):
    __tablename__ = 't_users'
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    username = db.Column(db.String(80),unique = True,nullable = False)
    email = db.Column(db.String(120),unique = True)
    password = db.Column(db.String(127),nullable = False)#short passwd for pbkdf2
    # password = db.Column(db.String(511),nullable = False)
    ### long passwd for scrypt BUT database cannot be changed by this comment
    posts = db.relationship('Post',backref = 'author',lazy = True)
    def __repr__(self):
        return '<User %r>' %self.username
    
class Post(TimestampMixin,db.Model):
    __tablename__ = 't_posts'
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    title = db.Column(db.String(225),nullable = False)
    abstract = db.Column(db.String(225),nullable = False)
    content = db.Column(db.Text,nullable = False)
    content_html = db.Column(db.Text,nullable = False)
    author_id = db.Column(db.Integer,db.ForeignKey('t_users.id'),nullable = False)
    

@login_manager.user_loader
def load_user(userid):
    return User.query.filter_by(id = userid).first()
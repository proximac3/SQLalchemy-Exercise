"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()

def connect_db(app):
    """Connect to database"""
    db.app = app
    db.init_app(app)


class Person(db.Model):
    """User Model"""

    __tablename__ = "person"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(), nullable=False, unique=True)
    last_name = db.Column(db.String(), nullable=False, unique=True)
    image_url = db.Column(db.String(), nullable=False)

    post = db.relationship('BlogPost', backref='Person')

    def __repr__(self):
        p = self
        return f"<user id= {p.id} first_name= {p.first_name} last_name= {p.last_name} image_url= {p.image_url}>"



class BlogPost(db.Model):
    """ Blog Post Model """
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False, unique=True)
    content = db.Column(db.String, nullable=False)
    time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    user = db.Column(db.Integer, db.ForeignKey('person.id'))

    users = db.relationship('Person', backref='posts')

    def __repr__(self):
        return f'<Post id={self.id} title={self.title} content={self.content} >'


class Tags(db.Model):
    """ Tags """

    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True)

    tag_rel = db.relationship('BlogPost', secondary='posttags', backref='tags')
    post_tag = db.relationship('PostTags', backref='tags')

    def __repr__(self):
        return f'<Tags id={self.id} name={self.name}>'


class PostTags(db.Model):
    """ Post Tags """

    __tablename__='posttags'

    post_title = db.Column(db.String(), db.ForeignKey('posts.title'), primary_key=True, nullable=False)
    tag_name = db.Column(db.String(), db.ForeignKey('tags.name'), primary_key=True, nullable=False)

    def __repr__(self):
        return f'<PostTags post_title={self.post_title} Tag_name={self.tag_name}>'

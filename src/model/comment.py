from google.appengine.ext import db
from src.model.post import Post
from src.model.user import User


class Comment(db.Model):
    """
    This class represents the 'Comment' entity. It references one post and has one owner.
    """
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    post_id = db.ReferenceProperty(Post, required=True)
    owner_id = db.ReferenceProperty(User, required=True)

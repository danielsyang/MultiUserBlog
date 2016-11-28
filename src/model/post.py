from google.appengine.ext import db
from src.handler import Handler
from src.model.user import User


class Post(db.Model):
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    owner_id = db.ReferenceProperty(User, required=True)

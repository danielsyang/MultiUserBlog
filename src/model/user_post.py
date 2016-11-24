from google.appengine.ext import db
from src.model.user import User
from src.model.post import Post

'''
This class describe the Many to Many relationship between users and posts.
One user can like many posts.
One post can be liked by many users.
'''


class UserPost(db.Model):
    user_id = db.ReferenceProperty(User,
                                   required=True)
    post_id = db.ReferenceProperty(Post,
                                   required=True)

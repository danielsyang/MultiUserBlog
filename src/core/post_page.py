from src.handler import Handler
from src.model.post import Post
from google.appengine.ext import db


class PostPage(Handler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id))
        post = db.get(key)

        if post:
            self.render("blog/post_blog.html", post=post)
        else:
            self.error(404)
            return

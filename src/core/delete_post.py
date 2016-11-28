from google.appengine.ext import db
from src.handler import Handler
from src.model.comment import Comment


class DeletePost(Handler):
    def get(self, post_id):
        if self.user:
            key = db.Key.from_path('Post', int(post_id))
            post = db.get(key)
            post.delete()
            self.render("blog/front_blog.html", status='Post deleted!')
        else:
            self.redirect('/login')

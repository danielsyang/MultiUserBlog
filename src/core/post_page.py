from src.handler import Handler
from src.model.post import Post
from src.model.comment import Comment
from google.appengine.ext import db


class PostPage(Handler):
    def get(self, post_id):
        if self.user:
            key = db.Key.from_path('Post', int(post_id))
            post = db.get(key)
            comment = Comment.all().filter('post_id = ', post.key())

            if post:
                self.render("blog/post_blog.html", post=post, comment=comment)
            else:
                self.error(404)
        else:
            self.redirect('/login')

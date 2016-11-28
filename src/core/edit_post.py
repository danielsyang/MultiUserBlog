from src.handler import Handler
from src.model.post import Post
from google.appengine.ext import db


class EditPost(Handler):
    def get(self, post_id):
        if self.user:
            key = db.Key.from_path('Post', int(post_id))
            post = db.get(key)
            self.render("blog/new_post.html", subject=post.subject, content=post.content, post_id=post.key().id())
        else:
            self.redirect('/login')

    def post(self, post_id):
        if self.user:
            key = db.Key.from_path('Post', int(post_id))
            post = db.get(key)

            subject = self.request.get('subject')
            content = self.request.get('textarea')

            post.subject = subject
            post.content = content

            post.put()
            self.redirect('/blog/post/%s' % str(post_id))
        else:
            self.redirect('/login')

from google.appengine.ext import db
from src.handler import Handler
from src.model.comment import Comment


class CommentPost(Handler):
    def post(self):
        if self.user:
            comment_input = self.request.get("commentInput")
            post_id = self.request.get("postID")

            key = db.Key.from_path('Post', int(post_id))
            post = db.get(key)

            if comment_input:
                c = Comment(content=comment_input, post_id=post.key(), owner_id=self.user.key())
                c.put()
                self.redirect('/blog/post/%s' % str(post.key().id()))
            else:
                error = "Comment is blank!"
                self.render('/blog/post/%s' % str(post.key().id()), error=error)
        else:
            self.redirect('/login')

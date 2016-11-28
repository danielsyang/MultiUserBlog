from google.appengine.ext import db
from src.handler import Handler
from src.model.comment import Comment


class DeleteComment(Handler):
    def get(self, comment_id):
        if self.user:
            key = db.Key.from_path('Comment', int(comment_id))
            comment = db.get(key)

            if self.user.key().id() == comment.owner_id.key().id():
                comment.delete()
            else:
                self.render("blog/front_blog.html", status="Error! This is not your comment.")           

        else:
            self.redirect('/login')

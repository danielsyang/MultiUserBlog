from google.appengine.ext import db
from src.handler import Handler
from src.model.comment import Comment


class EditComment(Handler):
    def get(self, comment_id):
        if self.user:
            key = db.Key.from_path('Comment', int(comment_id))
            comment = db.get(key)

            if self.user.key().id() == comment.owner_id.key().id():
                self.render("blog/edit_comment.html", content=comment.content,
                            comment_id=comment.key().id())
            else:
                self.render("blog/edit_comment.html", content=comment.content,
                            comment_id=comment.key().id(), error="You can't edit this post.")
        else:
            self.redirect('/login')

    def post(self):
        if self.user:
            comment_id = self.request.get("comment_id")
            comment_input = self.request.get("comment_input")

            key = db.Key.from_path('Comment', int(comment_id))
            comment = db.get(key)

            if self.user.key().id() == comment.owner_id.key().id():
                comment.content = comment_input
                comment.put()
            else:
                self.render("blog/edit_comment.html", content=comment.content,
                            comment_id=comment.key().id(), error="Error! Something went wrong!")

        else:
            print 'ooi'

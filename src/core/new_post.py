from src.handler import Handler
from src.model.post import Post


class NewPost(Handler):
    def get(self):
        if self.user:
            self.render("blog/new_post.html")
        else:
            self.redirect('/login')

    def post(self):
        subject = self.request.get("subject")
        text_area = self.request.get("textarea")

        if subject and text_area:
            p = Post(subject=subject, content=text_area, owner_id=self.user.key())
            p.put()
            self.redirect('/blog/post/%s' % str(p.key().id()))
        else:
            error = "Subject or Blog is invalid!"
            self.render("blog/new_post.html", error=error)

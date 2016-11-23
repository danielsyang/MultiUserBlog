from src.handler import Handler
from src.model.post import Post


class NewPost(Handler):
    def get(self):
        self.render("blog/new_post.html")

    def post(self):
        subject = self.request.get("subject")
        text_area = self.request.get("textarea")

        if subject and text_area:
            p = Post(subject=subject, content=text_area)
            p.put()
            self.redirect('/blog/%s' % str(p.key().id()))
        else:
            error = "Subject or Blog is invalid!"
            self.render("blog/new_post.html", error=error)
            # p.put()

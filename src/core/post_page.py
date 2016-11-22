from src.handler import Handler
from src.model.post import Post

class PostPage(Handler):
    def get(self):
        self.render("blog/post_blog.html")

    def post(self):
        subject = self.request.get("subject")
        text_area = self.request.get("textarea")

        if subject and text_area:
            p = Post(subject=subject, content=text_area)
            print p
        else:
            error = "Subject or Blog is invalid!"
            self.render("blog/post_blog.html", error=error)
            # p.put()

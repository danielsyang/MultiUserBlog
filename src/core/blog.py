from src.handler import Handler
from src.model.post import Post


class Blog(Handler):
    def get(self):
        if self.user:
            posts = Post.all().order('-created')
            self.render('blog/front_blog.html', posts=posts)
        else:
            self.redirect('/login')

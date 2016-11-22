from src.handler import Handler
from src.model.post import Post


class Blog(Handler):
    def get(self):
        if self.user:
            posts = Post.all().order('-created')
            self.render('blog/index.html', posts=posts)
        else:
            self.redirect('/login')

            # def post(self):
            #     print 'WTF!'

from src.handler import Handler


class Blog(Handler):
    def get(self):
        if self.user:
            self.render('blog/index.html')
        else:
            self.redirect('/login')

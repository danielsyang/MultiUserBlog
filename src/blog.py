from src.handler import Handler


class Blog(Handler):
    def get(self):
        self.render('blog/index.html')
from google.appengine.ext import db
from src.handler import Handler


class Post(db.Model):
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)

    # def render(self):
    #     self._render_text = self.content.replace('\n', '<br>')
    #     return Handler.render_str("html", p = self)

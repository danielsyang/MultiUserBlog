import webapp2

from src.core.blog import Blog
from src.index import Index
from src.login import Login
from src.signup import Signup
from src.logout import Logout

app = webapp2.WSGIApplication(
    [('/', Index),
     ('/login', Login),
     ('/signup', Signup),
     ('/blog', Blog),
     ('/logout', Logout)],
    debug=True)

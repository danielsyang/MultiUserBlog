import webapp2
from src.user_account.index import Index
from src.user_account.login import Login
from src.user_account.signup import Signup

from src.core.blog import Blog
from src.user_account.logout import Logout

app = webapp2.WSGIApplication(
    [('/', Index),
     ('/login', Login),
     ('/signup', Signup),
     ('/blog', Blog),
     ('/logout', Logout)],
    debug=True)

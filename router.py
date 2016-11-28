import webapp2
from src.user_account.index import Index
from src.user_account.login import Login
from src.user_account.signup import Signup
from src.user_account.logout import Logout
from src.core.blog import Blog
from src.core.new_post import NewPost
from src.core.post_page import PostPage
from src.core.my_post import MyPost
from src.core.comment_post import CommentPost
from src.core.edit_post import EditPost
from src.core.delete_post import DeletePost
from src.core.delete_comment import DeleteComment
from src.core.edit_comment import EditComment


app = webapp2.WSGIApplication(
    [('/', Index),
     ('/login', Login),
     ('/signup', Signup),
     ('/logout', Logout),
     ('/blog', Blog),
     ('/blog/my', MyPost),
     ('/blog/delete/([0-9]+)', DeletePost),
     ('/blog/post', NewPost),
     ('/blog/post/([0-9]+)', PostPage),
     ('/blog/comment', CommentPost),
     ('/blog/post/edit/([0-9]+)', EditPost),
     ('/blog/comment/delete/([0-9]+)', DeleteComment),
     ('/blog/comment/edit', EditComment)],
    debug=True)

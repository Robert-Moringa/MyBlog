import unittest

from ..app.models import Comment

class BlogTest(unittest.TestCase):
    def setUp(self):
        self.new_blog = Comment(comment = 'We live and die in Kenya')

import unittest

from ..app.models import Blog

class BlogTest(unittest.TestCase):
    def setUp(self):
        self.new_blog = Blog(title = 'Kenya Patriats', message = 'We live and die in Kenya', category = 'Leadership')

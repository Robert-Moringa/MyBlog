import unittest

from app.models import Blog

class BlogTest(unittest.TestCase):
    def setUp(self):
        self.new_blog = Blog(title = 'Kenya Patriats', message = 'We live and die in Kenya', category = 'Leadership')

    def test_delete_comment(self):
        '''
        test_delete_blog_post to test if we can remove a blog post
        '''
        self.new_account.save_blog()
        test_account = Blog(title = 'Kenya Patriats', message = 'We live and die in Kenya', category = 'Leadership')
        test_account.save()

        self.new_account.delete_blogpodt()
        self.assertEqual(len(Blog.accounts_list), 1)
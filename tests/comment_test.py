import unittest

from app.models import Comment

class BlogTest(unittest.TestCase):
    def setUp(self):
        self.new_blog = Comment(comment = 'We live and die in Kenya')

    def test_delete_comment(self):
        '''
        test_delete_comment to test if we can remove a comment
        '''
        self.new_account.add_comment()
        test_account = Comment('We live and die in Kenya')
        test_account.save()

        self.new_account.delete_comment()
        self.assertEqual(len(Comment.accounts_list), 1)


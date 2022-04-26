import unittest
from user import Users


class TestUser(unittest.TestCase):
    def setUp(self):
        "setup to test class"

        self.new_user = Users("bruno", "chino","1234")

    def test_create_user(self):
        '''test if user was instantiated correctly'''

        self.assertEqual(self.new_user.firstname, "bruno")
        self.assertEqual(self.new_user.username, "chino")
        self.assertEqual(self.new_user.password,"1234")

    def tes
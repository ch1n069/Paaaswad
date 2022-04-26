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

    def test_save_user(self):
        '''check if object is saved to the use account'''
        self.assertEqual(len(Users.user_list),0)
        self.new_user.save_user()
        self.assertEqual(len(Users.user_list),1)


    def test_delete_user(self):
        '''check if user is deleted from the use account'''
        self.assertEqual(len(Users.user_list),0)
        

    
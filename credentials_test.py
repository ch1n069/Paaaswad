import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    def setUp(self):

        '''set up method for test credentials'''

        self.new_credentials = Credentials("insta","chino","1234")

    def test_init(self):
        '''tesst if scredentials is created'''

        self.assertEqual(self.new_credentials.platform, "insta")
        self.assertEqual(
            self.new_credentials.user_account_username,"chino")
        self.assertEqual(
            self.new_credentials.account_password,"1234")


    def test_save_credentials(self):
        '''checkk if credtials are saved'''

        self.assertEqual(len(Credentials.user_credentials), 0)
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.user_credentials),1)

    def test_delete_credentials(self):
        '''check if credential has been deleted'''

        self.assertEqual(len(Credentials.user_credentials),0)
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.user_credentials),1)
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.user_credentials),0)



    def test_find_by_platform(self):
        '''check if we can find credential by platfrom'''
        self.found_credentials = Credentials.find_by_platform("insta")


if __name__ == "__main__":
    unittest.main()



        
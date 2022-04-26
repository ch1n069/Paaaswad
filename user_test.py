import unittest
from user import Users


class TestUser(unittest.TestCase):
    def setUp(self):
        "setup to test class"

        self.new_user = Users("bruno")
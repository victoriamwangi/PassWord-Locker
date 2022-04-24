import unittest
from user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        """
        define instructions that will be executed before each test method
        """
        self.user = User("vic", "hehe")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.user.userName, "vic")
        self.assertEqual(self.user.password, "hehe")


if __name__ == "__main__":
    unittest.main()

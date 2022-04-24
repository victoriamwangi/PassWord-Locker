import unittest
from credentials import Credential


class TestCredential(unittest.TestCase):

    def tearDown(self):
        Credential.accountsList = []

    def setUp(self):
        self.newCredential = Credential("twitter", "0000")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.newCredential.accountName, "twitter")
        self.assertEqual(self.newCredential.password, "0000")

    def test_saveCredential(self):
        self.newCredential.saveCredential()
        self.assertEqual(len(Credential.accountsList), 1)

    def test_deleteCredential(self):
        '''
            test deleteCredential to test if we can remove an account from our accounts list
        '''
        self.newCredential.saveCredential()
        testCredential = Credential("vic", "2222")
        testCredential.saveCredential()
        self.newCredential.deleteCredential()
        self.assertEqual(len(Credential.accountsList), 1)


if __name__ == "__main__":
    unittest.main()

from cgi import test
import unittest
from credentials import Credential


class TestCredential(unittest.TestCase):

    def tearDown(self):
        Credential.accountsList = []

    def setUp(self):
        self.newCredential = Credential("twitter", "vic", "0000")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.newCredential.accountName, "twitter")
        self.assertEqual(self.newCredential.password, "0000")
        self.assertEqual(self.newCredential.userName, "vic")

    def test_saveCredential(self):
        self.newCredential.saveCredential()
        self.assertEqual(len(Credential.accountsList), 1)

    def test_deleteCredential(self):
        '''
            test deleteCredential to test if we can remove an account from our accounts list
        '''
        self.newCredential.saveCredential()
        testCredential = Credential("twitter", "vic", "2222")
        testCredential.saveCredential()
        self.newCredential.deleteCredential()
        self.assertEqual(len(Credential.accountsList), 1)

    def test_findAccount(self):
        '''
        test to check if we can return a Boolean  if we cannot find the account.
        '''
        self.newCredential.saveCredential()
        testCredential = Credential("twitter", "vic", "2222")
        testCredential.saveCredential()
        foundCredential = Credential.findAccount("twitter")
        self.assertEqual(foundCredential.accountName,
                         testCredential.accountName)

    def test_accountExist(self):
        self.newCredential.saveCredential()
        testCredential = Credential("twitter", "vic", "0000")
        testCredential.saveCredential()
        credentialExist = Credential.account_exists("twitter")
        self.assertTrue(credentialExist)


if __name__ == "__main__":
    unittest.main()

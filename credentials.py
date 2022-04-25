import string
import secrets


class Credential:

    accountsList = []

    def __init__(self, accountName, userName, password):
        self.accountName = accountName
        self.password = password
        self.userName = userName
    pass

    def saveCredential(self):
        '''
        this method saves account objects into accountsList
        '''
        Credential.accountsList.append(self)

    # def newAccountCredentials(account, username, password, autogenerate):
    #     if(autogenerate):
    #         alphabet = string.ascii_letters + string.digits
    #         password = ''.join(secrets.choice(alphabet)for i in range(6))
    #     cred = Credential(account, username, password)
    #     Credential.accountsList.append(cred)

    def deleteCredential(self):
        '''
        deleteCredential method deletes a saved account from the accountsList
        '''
        Credential.accountsList.remove(self)

    def displayAccounts(cls):
        '''
        method that returns the accounts list
        '''
        return cls.accountsList

    @classmethod
    def findAccount(cls, name):
        for account in cls.accountsList:
            if account.accountName == name:
                return account

    @classmethod
    def account_exists(cls, name):
        for account in cls.accountsList:
            if account.accountName == name:
                return True
        return False

from operator import truediv


class Credential:

    accountsList = []

    def __init__(self, accountName, password):
        self.accountName = accountName
        self.password = password
    pass

    def saveCredential(self):
        '''
        this method saves account objects into accountsList
        '''
        Credential.accountsList.append(self)

    def deleteCredential(self):
        '''
        deleteCredential method deletes a saved account from the accountsList
        '''
        Credential.accountsList.remove(self)

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

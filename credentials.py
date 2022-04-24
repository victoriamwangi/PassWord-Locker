class Credential:

    accountsList = []

    def __init__(self, accountName, password):
        self.accountName = accountName
        self.password = password
    pass

    def saveAccount(self):
        '''
        this method saves account objects into accountsList
        '''
        Credential.accountsList.append(self)

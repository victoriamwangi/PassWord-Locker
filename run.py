from user import User
from credentials import Credential


def createUser(userName, password):
    newUser = User(userName, password)
    return newUser


def saveAcccount(account):
    '''
    Function to save account
    '''
    account.saveCredentials()


def delAccount(account):
    '''
    Function to delete account
    '''
    account.deleteCredential()


def find_account(name):
    '''
    Function to search account
    '''
    return Credential.findAccount(name)


def accountExist(name):
    '''
    Function to search account
    '''
    return Credential.account_exists()

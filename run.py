from user import User
from credentials import Credential


def createUsers(userName, password):
    '''
    Function to create user 
    '''
    newUser = User(userName, password)
    return newUser


def createAccount(accountName, userName, password):
    '''
    Function to create credentials of a spefic account
    '''
    newAccount = Credential(accountName, userName, password)
    return newAccount


def saveAcccount(account):
    '''
    Function to save account
    '''
    account.saveCredential()


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


def displayAccounts():
    '''
    Function that returns all the saved accounts
    '''
    return Credential.displayAccounts()


def main():
    print('Hello welcome to AppLock')
    user_name = input()

    print(f"Hello {user_name}. Well ")
    print('\n')

    while True:
        print("Use these short codes: cc- create applock account, lg- login, ca- create account credentials, da: delete account, da: display all accounts, fa: find specific account using account name")
        short_code = input().lower()
        if short_code == 'ca':
            print("Account type eg twitter")
            accountName = input()
            print('userName')
            userName = input()
            print("Input your password")
            passWord = input()
            saveAcccount(createAccount(accountName, userName, passWord))
            print('\n')
        elif short_code == 'da':
            if displayAccounts():
                print("Here is a list of all your accounts")
                print('/n')
                for account in displayAccounts():
                    print(
                        f"{account.accountName} {account.userName} {account.password}")
                    print('/n')
            else:
                print('/n')
                print("You don't have any accounts yet")
                print('/n')
        elif short_code == "fa":
            print("Enter the accounts name eg twitter")
            searchAccount = input()
            if accountExist(searchAccount):
                searchAccount = find_account(searchAccount)
                print(
                    f"{searchAccount.accountName} {searchAccount.userName} {searchAccount.password}")
            else:
                print("This account doesn't exist")
        elif short_code == "ex":
            print("It was good to see you")
            break
        else:
            print("Wrong short code, enter the correct short code")


if __name__ == "__main__":
    main()

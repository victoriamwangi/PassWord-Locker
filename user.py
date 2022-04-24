#!/usr/bin/env python3.9
class User:
    user = None

    def __init__(self, userName, password):
        self.userName = userName
        self.password = password

    pass

    def saveUser(self):
        """
        Create and save a user in variable user
        """
        self.user = self

    def login(self):
        if (self.user is self):
            return "iyete"
        else:
            return "ziii"

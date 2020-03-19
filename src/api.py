#!/usr/bin/env python3

import json
from pprint import pprint
from pymongo import MongoClient

class Api:
    '''
    The API class implements the Innoventory API which is used to interact
    with the backend MongoDB instance. 
    '''
    authenConnectionString = "mongodb+srv://AuthenTest:test@innoventory-vvoxp.azure.mongodb.net/test?retryWrites=true&w=majority"
    customerConnectionString = ""
    employeeConnectionString = ""
    managerConnectionString = ""

    emptyUser = {'username': '', 'password': ''}

    # connect to a database using a valid connection string and return client
    def connect(self, connectionString=""):
        self.connectionString = connectionString
        client = MongoClient(connectionString)
        return client

    def authenticate(self, user={}):
        self.user = user

    def search(self):
        pass
    

class Login(Api):
    '''
    The Login class provides the functionality to query the MongoDB instance
    to authenticate a user.
    '''

    '''
    The checkPassword method accepts a dictionary containing the username and password
    of the user to be authenticated. If the username and password are valid and correct,
    the user's information is returned as a dictionary. If the username and/or password
    are not correct, an Api.emptyUser dictionary is returned.
    '''
    def checkPassword(self, user={'username': '', 'password': ''}):
        self.user = user
        validPassword = False
        # Get connection to database
        client = self.connect(Api.authenConnectionString)
        # Switch to Authen database
        db = client.Authen
        # Switch to Users collection in Authen database
        collection = db.Users
        # search for user
        # returns a single document or None if there is no match
        userInfo = collection.find_one({'username':self.user['username']})

        # if found, check to see if password matches
        if userInfo != None:
            # check password retrieved from database vs input password
            if userInfo['password'] == self.user['password']:
                validPassword = True

            # Password tests
            if validPassword:
                print("Valid username, valid password")
            else:
                print("Valid username, invalid password")
                userInfo = Api.emptyUser
        else:
            print("Username does not exist")
            userInfo = Api.emptyUser

        return userInfo

    '''
    The login method accepts a user dictionary containing the username and password.
    The password is checked and the userInfo object is returned.
    '''
    def login(self, user={'username': '', 'password': ''}):
        self.user = user
        userInfo = self.checkPassword(self.user)

        return userInfo

    
        
        


# If api.py is run on its own, all tests will be run and the results will be shown
if __name__ == "__main__":
    validTestUser = {'username':'bwalker', 'password':'GC2020'}
    invalidPassword = {'username':'bwalker', 'password':'wrong'}
    invalidUsername = {'username':'bwekrlkd', 'password':'doesntmatter'}

    # Login tests
    loginTest = Login()
    # Valid username and password test
    user = loginTest.login(validTestUser)
    pprint(user)
    # Valid username, invalid password test
    user = loginTest.login(invalidPassword)
    pprint(user)
    # Invalid username, Invalid password
    user = loginTest.login(invalidUsername)
    pprint(user)
    # No login information given
    user = loginTest.login()
    pprint(user)






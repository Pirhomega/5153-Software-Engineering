#!/usr/bin/env python3

import json
from pprint import pprint
from pymongo import MongoClient

class Api:
    '''
    The API class implements the Innoventory API which is used to interact
    with the backend MongoDB instance. 
    '''
    
    def connect(self, database=None, user=None):
        pass

    def authenticate(self, user=None):
        self.user = user

    def search(self):
        pass
    

class Login(Api):
    '''
    The Login class provides the functionality to query the MongoDB instance
    to authenticate a user.
    '''

    # connect to the Users collection in database Authen
    def connect(self, user={'username': '', 'password':''}):
        self.user = user
        validPassword = False

        # connect to main database
        client = MongoClient("mongodb+srv://AuthenTest:test@innoventory-vvoxp.azure.mongodb.net/test?retryWrites=true&w=majority")
        # switch to Authen database
        db = client.Authen
        # switch to Users collection
        collection = db.Users
        # search for user
        # returns a single document or None if there is no match
        userExists = collection.find_one({'username':self.user['username']})

        # if found, check to see if password matches
        if userExists != None:
            # check password in database vs given password
            if userExists['password'] == self.user['password']:
                validPassword = True

            # Password tests
            if validPassword:
                print("Valid username, valid password")
            else:
                print("Valid username, invalid password")
        else:
            print("Username does not exist")


if __name__ == "__main__":
    validTestUser = {'username':'bwalker', 'password':'GC2020'}
    invalidPassword = {'username':'bwalker', 'password':'wrong'}
    invalidUsername = {'username':'bwekrlkd', 'password':'doesntmatter'}

    # Login tests
    loginTest = Login()
    # Valid username and password test
    loginTest.connect(validTestUser)
    # Valid username, invalid password test
    loginTest.connect(invalidPassword)
    # Invalid username, Invalid password
    loginTest.connect(invalidUsername)






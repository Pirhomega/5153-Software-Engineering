#!/usr/bin/env python3

import json
import urllib.parse
from pprint import pprint
from pymongo import MongoClient

class Api:
    '''
    The API class implements the Innoventory API which is used to interact
    with the backend MongoDB instance. 
    '''
    authenUsername = urllib.parse.quote("AuthenTest")
    authenPassword = urllib.parse.quote("test")
    authenConnectionString = f"mongodb+srv://{authenUsername}:{authenPassword}@innoventory-vvoxp.azure.mongodb.net/test?retryWrites=true&w=majority"
    
    customerUsername = urllib.parse.quote("customer")
    customerPassword = urllib.parse.quote("gIcgQXd4prd1C3yk")
    customerConnectionString = f"mongodb+srv://{customerUsername}:{customerPassword}@innoventory-vvoxp.azure.mongodb.net/test?retryWrites=true&w=majority"
    
    employeeUsername = urllib.parse.quote("employee")
    employeePassword = urllib.parse.quote("")
    employeeConnectionString = f"mongodb+srv://{employeeUsername}:{employeePassword}@innoventory-vvoxp.azure.mongodb.net/test?retryWrites=true&w=majority"

    managerUsername = urllib.parse.quote("manager")
    managerPassword = urllib.parse.quote("")
    managerConnectionString = f"mongodb+srv://{managerUsername}:{managerPassword}@innoventory-vvoxp.azure.mongodb.net/test?retryWrites=true&w=majority"

    emptyUser = {'username': '', 'password': ''}

    # connect to a database using a valid connection string and return client
    def connect(self, connectionString=""):
        self.connectionString = connectionString
        client = MongoClient(connectionString)
        return client

    def authenticate(self, user={}):
        pass

    def create(self, document={}):
        pass

    # A test
    def searchGrocery(self, term):
        # The term to search for
        self.term = term
        # Get database connection client
        client = self.connect(self.customerConnectionString)
        # Switch to Innoventory database
        db = client.Innoventory
        # Search the Grocery collection
        result = db.Grocery.find_one(self.term)

        return result
    
    # search the product collection for a specific item
    def search(self, term):
        self.term = term
        client = self.connect(self.customerConnectionString)
        db = client.Innoventory
        # will hold all cursors from queries
        result = []
        # split the search term by whitespace
        new_search = self.term["item"].split()
        # search database by each word in term
        for word in new_search:
            # mini_result = db.Products.find({ "item": "/"+word+"/" })
            # result.append(mini_result)
            result.append(list(db.Products.find({ "item": {'$regex': word }})))
        return result
    # a simple print function for item names
    def display_results(self, search_result):
        for doc in search_result:
            for result in doc:
                print(result['item'])
    # Returns an unordered set of item names from a search
    def parse_results(self, search_result):
        # Use a set to avoid duplicate results
        items = set()
        for doc in search_result:
            for result in doc:
                items.add(result['item'])
        return items

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
    def authenticate(self, user={'username': '', 'password': ''}):
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

        #########################################################################
        login_success = False
        #########################################################################

        # if found, check to see if password matches
        if userInfo != None:
            # check password retrieved from database vs input password
            if userInfo['password'] == self.user['password']:
                validPassword = True

            # Password tests
            if validPassword:
                print("Valid username, valid password")
                login_success = True
            else:
                print("Valid username, invalid password")
                userInfo = Api.emptyUser
        else:
            print("Username does not exist")
            userInfo = Api.emptyUser

        return userInfo, login_success

    '''
    The login method accepts a user dictionary containing the username and password.
    The password is checked and the userInfo object is returned.
    '''
    def login(self, user={'username': '', 'password': ''}):
        self.user = user
        # returns the userInfo dictionary and a boolean, login_success
        return self.authenticate(self.user)

    
class UserManager(Api):
    '''
    The UserManager class contains methods for creating users and modifying
    '''

    # Connects to the Authen database and switches to the Users collection
    def connectToAuthen(self):
        # Get connection to MongoDB instance as the authen user
        client = self.connect(Api.authenConnectionString)
        # Connect to Authen db
        db = client.Authen
        # Switch to Users collection
        collection = db.Users      

        return collection 

    # The createUser method creates a new user if the given username is not already in use
    def createUser(self, data={}):
        self.data = data
        status = False

        collection = self.connectToAuthen()

        # Make sure username does not already exist
        # find_one returns None if the username is not in the Users collection
        userExists = collection.find_one({'username': self.data['username']})
        # If the username does not already exist, it is safe to create the new user
        if userExists == None:
            collection.insert_one(self.data)
            status = True

            # create the user's shopping cart in the 'Shopping_Cart' collection
            ShoppingCart(self.data).createCart()
        
        # Return true for successful user creation, false for user creation failure
        return status

    # The removeUser function removes a user account from the Users collection if it exists
    # The number of documents removed is returned as an integer value
    def removeUser(self, data={}):
        self.data = data
        status = 0
        
        collection = self.connectToAuthen()

        # If the username exists, remove it from the Users collection
        result = collection.delete_one(self.data)

        # remove user's shopping cart
        ShoppingCart(self.data).eraseUser()

        status = result.deleted_count

        return status

# This class represents all the shopping cart functionality
# See __main__ for example code
class ShoppingCart(Api):
    def __init__(self, user={'username': ''}):
        client = self.connect(Api.authenConnectionString)
        # Connect to Authen db
        db = client.Authen
        # Switch to Users collection
        self.collection = db.Shopping_Cart
        self.user = user

    # only call this when a user is creating an account
    def createCart(self):
        # create an empty array for cart items
        self.collection.insert_one({'username': self.user['username'], 'cart': []})

    # appends a dictionary to the 'cart' list (adds an item to the cart)
    # Example:
    #       shop_cart.addCart({'username': 'bwalker'}, {'item':'Dr. Pepper','quantity':1,'available':True})
    def addCart(self, item={}):
        self.item = item
        self.collection.update_one(
                self.user, 
                {'$push': {'cart': {'$each': [ self.item ]}}}
        )

    # removes an item from the user's cart
    # Example:
    #       shop_cart.removeCart({'username': 'bwalker'}, {'item':'Dr. Pepper'})   
    def removeCart(self, item={}):
        self.item = item
        self.collection.update_one(
            self.user, 
            {'$pull': {'cart': self.item }}
        )
    
    # modify an item quantity
    def changeQuan(self, item={}, quantity=1):
        self.item = item
        self.quantity = quantity
        self.collection.update_one(
            filter=self.user,
            update={'$set': {f"cart.$[element].quantity": self.quantity}},
            array_filters=[{'element': self.item}]
        )
    
    # copies all shopping cart contents to a list
    def readShoppingcart(self):
        return dict(self.collection.find_one(filter=self.user))['cart']

    # erase user's cart
    def eraseUser(self):
        self.collection.delete_one(self.user)

# If api.py is run on its own, all tests will be run and the results will be shown
if __name__ == "__main__":
    import time
    validTestUser = {'username':'bwalker', 'password':'GC2020'}
    invalidPassword = {'username':'bwalker', 'password':'wrong'}
    invalidUsername = {'username':'bwekrlkd', 'password':'doesntmatter'}

    # Login tests
    print("*****LOGIN TESTS*****")
    loginTest = Login()
    
    # Valid username and password test
    user, login_success = loginTest.login(validTestUser)
    pprint(user)

    # Valid username, invalid password test
    user, login_success = loginTest.login(invalidPassword)
    pprint(user)

    # Invalid username, Invalid password
    user, login_success = loginTest.login(invalidUsername)
    pprint(user)

    # No login information given
    user, login_success = loginTest.login()
    pprint(user)

    print("*****CONNECTION TESTS*****")
    # Connection tests
    api = Api()
    connect1 = api.connect(api.customerConnectionString)
    testSearch = api.searchGrocery({'item':'Clam Nectar'})
    pprint(testSearch)
    print("*****CREATE USER TEST*****")
    userTest = UserManager()

    # Create a user that doesn't exist
    result = userTest.createUser({'username': 'test', 'password': 'test'})
    print(f"Create user account (should be True): {result}")
    time.sleep(5)

    # Remove the user that was just created
    result = userTest.removeUser({'username': 'test'})
    print(f"Delete a user account (should be 1): {result}")
    time.sleep(5)

    # Try to create a user using a username that is taken already
    result = userTest.createUser({'username': 'bwalker', 'password' : 'random'})
    print(f"Try to create a user with a username that's taken (should be False): {result}")
    time.sleep(5)

    # Try to delete a user that doesn't exist
    result = userTest.removeUser({'username': 'test'})
    print(f"Try to delete an account that doesn't exist (should be 0): {result}")
    
    # Create a shopping cart for a user, add some items to it, remove items from it, erase the user's cart completely
    shop_cart = ShoppingCart({'username': 'cmat'})
    shop_cart.createCart()
    shop_cart.addCart({'item':'coke','quantity':1234,'available':True})
    shop_cart.addCart({'item':'Sprite','quantity':12,'available':False})
    shop_cart.addCart({'item':'Dr. Pepper','quantity':1,'available':True})
    shop_cart.changeQuan({'item':'coke','quantity':1234,'available':True}, 1235)
    shop_cart.removeCart({'item':'Dr. Pepper'})
    shop_cart.removeCart({'item':'Sprite','quantity':12})
    print(shop_cart.readShoppingcart())
    print("Gimme sec")
    time.sleep(5)
    shop_cart.eraseUser()





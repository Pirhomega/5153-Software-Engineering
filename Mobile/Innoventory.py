#!/usr/bin/env python3

import api
import copy
import decimal
import pymongo
import urllib.parse
import pprint

# Kivy imports are now in alphabetical order
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty, ListProperty, BooleanProperty, StringProperty

# Kivy uix imports
from kivy.uix.behaviors import ButtonBehavior, FocusBehavior
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.recyclegridlayout import RecycleGridLayout 
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.layout import LayoutSelectionBehavior 
from kivy.uix.recycleview.views import RecycleDataViewBehavior 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

# Set the window size for the application
Window.size = (450, 800)
# PrettyPrinter for json
pp = pprint.PrettyPrinter(indent=4)
# Some global user information for the session
username = ""
shopCartInfo = []
dbInfo = []

# These classes are for screens or screen behavior. Any class with the pass keyword
# is defined and manipulated in the .kv file, but the prototype must be in this file
# as well.
class Img(Image):
    pass

class FloatLay(FloatLayout):
    pass

class GridLay(GridLayout):
    pass

class WindowManager(ScreenManager):
    pass

class ImgButton(ButtonBehavior,Image):
    pass

class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior, RecycleGridLayout):
    pass

class CheckoutPopup(FloatLayout):
    pass 


'''
$$\                           $$\           
$$ |                          \__|          
$$ |       $$$$$$\   $$$$$$\  $$\ $$$$$$$\  
$$ |      $$  __$$\ $$  __$$\ $$ |$$  __$$\ 
$$ |      $$ /  $$ |$$ /  $$ |$$ |$$ |  $$ |
$$ |      $$ |  $$ |$$ |  $$ |$$ |$$ |  $$ |
$$$$$$$$\ \$$$$$$  |\$$$$$$$ |$$ |$$ |  $$ |
\________| \______/  \____$$ |\__|\__|  \__|
                    $$\   $$ |              
                    \$$$$$$  |              
                     \______/               
'''
class Login(Screen):
    '''
    The Login class implements the login screen from which a user can login or
    navigate to the create account screen.
    '''

    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def login(self):
        # Get an instance of the login class from the api
        login = api.Login()

        global username
        
        self.username =  urllib.parse.quote(self.usernameIn.text) # passwordHell
        self.password =  urllib.parse.quote(self.passwordIn.text) # XR9lYeOp036C%@&@cQn*8z3BU4\

        username = self.username
        
        try:
            # Will return a dictionary of user information. If the username and/or password
            # are wrong, an emtpy username and password are returned
            result, success, customer = login.login({'username': self.username, 'password': self.password})
            
            if(result['username'] != "" and result['password'] != "" and customer == True):
                # If the login is successful, take the user to the homepage window
                wm.current = "homepage"
            else:
                # Create a popup window to display the authentication failure
                invalidLoginPopup = Popup(title="Authentication Failure", title_align="center", 
                    content=Label(text="Login Failed"), size_hint=(.75,.5))
                
                # Show the authentication failure popup
                invalidLoginPopup.open()

            # Reset the login page
            self.reset()
        except:
            print("Invalid login")

    # Removes input from text boxes
    def reset(self):
        self.usernameIn.text = ""
        self.passwordIn.text = ""
        
    #Do we need to create accounts if only superuser can add people?
    #Can you even make an account without signing up on atlas?
    def createAcct(self):
        self.reset()
        wm.current = "createAcct"

'''
$$\   $$\                                                                           
$$ |  $$ |                                                                          
$$ |  $$ | $$$$$$\  $$$$$$\$$$$\   $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  
$$$$$$$$ |$$  __$$\ $$  _$$  _$$\ $$  __$$\ $$  __$$\  \____$$\ $$  __$$\ $$  __$$\ 
$$  __$$ |$$ /  $$ |$$ / $$ / $$ |$$$$$$$$ |$$ /  $$ | $$$$$$$ |$$ /  $$ |$$$$$$$$ |
$$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$   ____|$$ |  $$ |$$  __$$ |$$ |  $$ |$$   ____|
$$ |  $$ |\$$$$$$  |$$ | $$ | $$ |\$$$$$$$\ $$$$$$$  |\$$$$$$$ |\$$$$$$$ |\$$$$$$$\ 
\__|  \__| \______/ \__| \__| \__| \_______|$$  ____/  \_______| \____$$ | \_______|
                                            $$ |                $$\   $$ |          
                                            $$ |                \$$$$$$  |          
                                            \__|                 \______/           
'''
class Homepage(Screen):
    '''
    The Homepage class implements the homepage screen from which a user can search 
    for items using the search bar, navigate to the shopping cart screen, the settings
    screen, or logout and return to the login screen.
    '''
    searchPhrase = ObjectProperty(None)
       
    def logout(self):
        global shopCartInfo
        # Clear user's shopping cart
        shopCartInfo = []
        # Remove any items left in the recycleview for the shopping cart screen
        wm.get_screen("shoppingCart").clear_recview()
        wm.current = "login"
    
    def settingsMenu(self):
        wm.current = "settingsMenu"

    def search(self):
        
        if(self.searchPhraseIn.text != ""):
            self.searchPhrase = self.searchPhraseIn.text
            #print(self.searchPhrase)
            self.searchPhraseIn.text = ""

            # Get an instance of the api
            apiSearch = api.Api()
            query = apiSearch.search({'item': self.searchPhrase})
            #apiSearch.display_results(query)

            #print("Parsed results")
            parsed_results = apiSearch.parse_results(query)
            # Check that there are results for the query
            resultBool = self.checkForResults(parsed_results)
            # print(parsed_results)
            
            if resultBool:
                # Show the query results in the SearchView
                wm.get_screen("searchView").send_query_results(query, parsed_results)
                wm.get_screen("prodInfo").send_query_results(query, parsed_results)
                wm.current = "searchView"
            else:
                wm.current = "homepage"

    # If a query has at least one result, returns True. If a query has no 
    # results, returns False and creates a popup       
    def checkForResults(self, parsed_results):
        # Check if there are no results
        if not parsed_results:
            # Create a popup
            noResults = Popup(title="No results", title_align="center", 
                content=Label(text="No matches for your query"), 
                size_hint=(.75,.5))
            # Show the authentication failure popup
            noResults.open()
            return False
        else:
            return True

'''
 $$$$$$\                                  $$\                $$$$$$\                                                      $$\     
$$  __$$\                                 $$ |              $$  __$$\                                                     $$ |    
$$ /  \__| $$$$$$\   $$$$$$\   $$$$$$\  $$$$$$\    $$$$$$\  $$ /  $$ | $$$$$$$\  $$$$$$$\  $$$$$$\  $$\   $$\ $$$$$$$\  $$$$$$\   
$$ |      $$  __$$\ $$  __$$\  \____$$\ \_$$  _|  $$  __$$\ $$$$$$$$ |$$  _____|$$  _____|$$  __$$\ $$ |  $$ |$$  __$$\ \_$$  _|  
$$ |      $$ |  \__|$$$$$$$$ | $$$$$$$ |  $$ |    $$$$$$$$ |$$  __$$ |$$ /      $$ /      $$ /  $$ |$$ |  $$ |$$ |  $$ |  $$ |    
$$ |  $$\ $$ |      $$   ____|$$  __$$ |  $$ |$$\ $$   ____|$$ |  $$ |$$ |      $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |  $$ |$$\ 
\$$$$$$  |$$ |      \$$$$$$$\ \$$$$$$$ |  \$$$$  |\$$$$$$$\ $$ |  $$ |\$$$$$$$\ \$$$$$$$\ \$$$$$$  |\$$$$$$  |$$ |  $$ |  \$$$$  |
 \______/ \__|       \_______| \_______|   \____/  \_______|\__|  \__| \_______| \_______| \______/  \______/ \__|  \__|   \____/                                                                                                                                                                                                                                                                                                                                                                                                  
'''
class CreateAccount(Screen):
    '''
    The CreateAccount class implements the create account screen. This screen allows a user to input a desired username
    and password combination. If the username is not take, a new account will be created. If the username is taken,
    the user will be prompted to input a new username.
    '''
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def createAccount(self):
        self.username =  urllib.parse.quote(self.usernameIn.text)
        self.password =  urllib.parse.quote(self.passwordIn.text)

        # Get a UserManager object
        user = api.UserManager()
        # Create the user
        if self.username == "" or self.password == "":
            valid_input = False
        else:
            valid_input = True

        # Returns True if the user was successfully created
        if valid_input == True:
            result = user.createUser({'username': self.username, 'password': self.password})
        else:
            result = False

        if result == True:
            wm.current = "homepage"
        else:
            # Create a popup window to display the authentication failure
            failedUserCreationPopup = Popup(title="User Creation Failure", title_align="center", 
                content=Label(text="User Creation Failed\n Username Taken"), size_hint=(.75,.5))
                
            # Show the authentication failure popup
            failedUserCreationPopup.open()

        self.reset()

    # Removes input from text boxes
    def reset(self):
        self.usernameIn.text = ""
        self.passwordIn.text = ""



'''
 $$$$$$\             $$\     $$\     $$\                               $$\      $$\                               
$$  __$$\            $$ |    $$ |    \__|                              $$$\    $$$ |                              
$$ /  \__| $$$$$$\ $$$$$$\ $$$$$$\   $$\ $$$$$$$\   $$$$$$\   $$$$$$$\ $$$$\  $$$$ | $$$$$$\  $$$$$$$\  $$\   $$\ 
\$$$$$$\  $$  __$$\\_$$  _|\_$$  _|  $$ |$$  __$$\ $$  __$$\ $$  _____|$$\$$\$$ $$ |$$  __$$\ $$  __$$\ $$ |  $$ |
 \____$$\ $$$$$$$$ | $$ |    $$ |    $$ |$$ |  $$ |$$ /  $$ |\$$$$$$\  $$ \$$$  $$ |$$$$$$$$ |$$ |  $$ |$$ |  $$ |
$$\   $$ |$$   ____| $$ |$$\ $$ |$$\ $$ |$$ |  $$ |$$ |  $$ | \____$$\ $$ |\$  /$$ |$$   ____|$$ |  $$ |$$ |  $$ |
\$$$$$$  |\$$$$$$$\  \$$$$  |\$$$$  |$$ |$$ |  $$ |\$$$$$$$ |$$$$$$$  |$$ | \_/ $$ |\$$$$$$$\ $$ |  $$ |\$$$$$$  |
 \______/  \_______|  \____/  \____/ \__|\__|  \__| \____$$ |\_______/ \__|     \__| \_______|\__|  \__| \______/ 
                                                   $$\   $$ |                                                     
                                                   \$$$$$$  |                                                     
                                                    \______/                                                      
'''
class SettingsMenu(Screen):
    '''
    The SettingsMenu class implements the settings screen, which allows the user to modify
    their account. This can be added to as user account functionality increases.
    '''
    def changePassword(self):
        wm.current = "changePassword"



'''
 $$$$$$\  $$\                                                     $$$$$$$\                                                                       $$\ 
$$  __$$\ $$ |                                                    $$  __$$\                                                                      $$ |
$$ /  \__|$$$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\        $$ |  $$ |$$$$$$\   $$$$$$$\  $$$$$$$\ $$\  $$\  $$\  $$$$$$\   $$$$$$\   $$$$$$$ |
$$ |      $$  __$$\  \____$$\ $$  __$$\ $$  __$$\ $$  __$$\       $$$$$$$  |\____$$\ $$  _____|$$  _____|$$ | $$ | $$ |$$  __$$\ $$  __$$\ $$  __$$ |
$$ |      $$ |  $$ | $$$$$$$ |$$ |  $$ |$$ /  $$ |$$$$$$$$ |      $$  ____/ $$$$$$$ |\$$$$$$\  \$$$$$$\  $$ | $$ | $$ |$$ /  $$ |$$ |  \__|$$ /  $$ |
$$ |  $$\ $$ |  $$ |$$  __$$ |$$ |  $$ |$$ |  $$ |$$   ____|      $$ |     $$  __$$ | \____$$\  \____$$\ $$ | $$ | $$ |$$ |  $$ |$$ |      $$ |  $$ |
\$$$$$$  |$$ |  $$ |\$$$$$$$ |$$ |  $$ |\$$$$$$$ |\$$$$$$$\       $$ |     \$$$$$$$ |$$$$$$$  |$$$$$$$  |\$$$$$\$$$$  |\$$$$$$  |$$ |      \$$$$$$$ |
 \______/ \__|  \__| \_______|\__|  \__| \____$$ | \_______|      \__|      \_______|\_______/ \_______/  \_____\____/  \______/ \__|       \_______|
                                        $$\   $$ |                                                                                                   
                                        \$$$$$$  |                                                                                                   
                                         \______/                                                                                                    
'''
class ChangePassword(Screen):
    '''
    The ChangePassword class implements the ChangePassword screen, which allows the user to change their password.
    '''
    oldPassword = ObjectProperty(None)
    newPassword = ObjectProperty(None)
    newPassword2 = ObjectProperty(None)
    
    def back(self):
        wm.current = "settingsMenu"
    
    # Changes the user password
    def changePass(self):
        login = api.Login()
        manage = api.UserManager()

        self.oldPassword =  urllib.parse.quote(self.oldPasswordIn.text)
        self.newPassword =  urllib.parse.quote(self.newPasswordIn.text)
        self.newPassword2 =  urllib.parse.quote(self.newPasswordIn2.text)
        
        if(self.newPassword == self.newPassword2):
            # Pass the new and old data to the api
           result = manage.changePassword(
                {'username': username, 'password': self.oldPassword},
                {'username': username, 'password': self.newPassword})
        self.reset()
            
        if result == True:
            # Password change succesful popup
            passChangePopup = Popup(title="Success", title_align="center", 
                content=Label(text="Password Changed!"), size_hint=(.75,.5))
            passChangePopup.open()
        
        else:
            print("password change fail")
   
    # Removes input from text boxes
    def reset(self):
        self.oldPasswordIn.text = ""
        self.newPasswordIn.text = ""
        self.newPasswordIn2.text = ""

'''
 $$$$$$\                                          $$\      $$\    $$\ $$\                         
$$  __$$\                                         $$ |     $$ |   $$ |\__|                        
$$ /  \__| $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$$\ $$$$$$$\ $$ |   $$ |$$\  $$$$$$\  $$\  $$\  $$\ 
\$$$$$$\  $$  __$$\  \____$$\ $$  __$$\ $$  _____|$$  __$$\\$$\  $$  |$$ |$$  __$$\ $$ | $$ | $$ |
 \____$$\ $$$$$$$$ | $$$$$$$ |$$ |  \__|$$ /      $$ |  $$ |\$$\$$  / $$ |$$$$$$$$ |$$ | $$ | $$ |
$$\   $$ |$$   ____|$$  __$$ |$$ |      $$ |      $$ |  $$ | \$$$  /  $$ |$$   ____|$$ | $$ | $$ |
\$$$$$$  |\$$$$$$$\ \$$$$$$$ |$$ |      \$$$$$$$\ $$ |  $$ |  \$  /   $$ |\$$$$$$$\ \$$$$$\$$$$  |
 \______/  \_______| \_______|\__|       \_______|\__|  \__|   \_/    \__| \_______| \_____\____/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
'''
class SearchView(Screen,BoxLayout,GridLayout):
    '''
    The SearchView class implements the screen functionality for displaying a list of items
    returned from a search. This list of items is displayed using a Kivy recycleview with
    clickable buttons from the SearchButton class.
    '''
    full_data = ListProperty([])
    my_label = ListProperty([])

    def __init__(self, **kwargs):
        super(SearchView, self).__init__(**kwargs)
        #self.test()

    # Do a test search to show the recycleview functionality
    def test(self):
        # Get an instance of the api
        apiSearch = api.Api()
        # Do the search
        testSearch = apiSearch.search({'item': 'x'})
        # Print search results for testing
        apiSearch.display_results(testSearch)
        # Parse results to only have a list of items
        # The full detail of each item is still in testSearch at this point
        results = apiSearch.parse_results(testSearch)
        # Print list of items for testing
        # print(results)

        # A list comprehension that builds a list of strings of item names
        self.my_label = [{'text': str(item)} for item in results]

    def send_query_results(self, full_data=None, labels=None):
        self.full_data = full_data
        self.my_label = [{'text': str(item)} for item in labels]

   
'''
 $$$$$$\                                          $$\       $$$$$$$\              $$\     $$\                         
$$  __$$\                                         $$ |      $$  __$$\             $$ |    $$ |                        
$$ /  \__| $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$$\ $$$$$$$\  $$ |  $$ |$$\   $$\ $$$$$$\ $$$$$$\    $$$$$$\  $$$$$$$\  
\$$$$$$\  $$  __$$\  \____$$\ $$  __$$\ $$  _____|$$  __$$\ $$$$$$$\ |$$ |  $$ |\_$$  _|\_$$  _|  $$  __$$\ $$  __$$\ 
 \____$$\ $$$$$$$$ | $$$$$$$ |$$ |  \__|$$ /      $$ |  $$ |$$  __$$\ $$ |  $$ |  $$ |    $$ |    $$ /  $$ |$$ |  $$ |
$$\   $$ |$$   ____|$$  __$$ |$$ |      $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |  $$ |$$\ $$ |$$\ $$ |  $$ |$$ |  $$ |
\$$$$$$  |\$$$$$$$\ \$$$$$$$ |$$ |      \$$$$$$$\ $$ |  $$ |$$$$$$$  |\$$$$$$  |  \$$$$  |\$$$$  |\$$$$$$  |$$ |  $$ |
 \______/  \_______| \_______|\__|       \_______|\__|  \__|\_______/  \______/    \____/  \____/  \______/ \__|  \__|                                                                                                                                                                                                                                                                                                                                                                  
'''
class SearchButton(RecycleDataViewBehavior, Button):
    '''
    The SearchButton class is used for displaying search results as clickable buttons. Clicking or selecting a button
    will take the user to a new page with a detailed breakdown of the item's information. These buttons are used
    by the SearchView class to list all items returned from a search of the product database.
    '''
    # Extend recycle_view_attrs from the RecycleDataViewBehavior class
    def refresh_view_attrs(self, rec_view, my_index, data):
        self.my_index = my_index
        return super(SearchButton, self).refresh_view_attrs(rec_view, my_index, data)

    def apply_selection(self, rec_view, my_index, am_selected):
        self.selected = am_selected

    def on_press(self):
        item = self.text
        #print(f"LABEL: {item} ")
        # send the item the user clicks on to prodInfo
        wm.get_screen("prodInfo").sendItem(item)
        wm.transition.direction = "left"
        wm.current = "prodInfo"

    def update_changes(self, txt):
        pass


"""
$$$$$$$\                            $$\ $$$$$$\            $$$$$$\           
$$  __$$\                           $$ |\_$$  _|          $$  __$$\          
$$ |  $$ | $$$$$$\   $$$$$$\   $$$$$$$ |  $$ |  $$$$$$$\  $$ /  \__|$$$$$$\  
$$$$$$$  |$$  __$$\ $$  __$$\ $$  __$$ |  $$ |  $$  __$$\ $$$$\    $$  __$$\ 
$$  ____/ $$ |  \__|$$ /  $$ |$$ /  $$ |  $$ |  $$ |  $$ |$$  _|   $$ /  $$ |
$$ |      $$ |      $$ |  $$ |$$ |  $$ |  $$ |  $$ |  $$ |$$ |     $$ |  $$ |
$$ |      $$ |      \$$$$$$  |\$$$$$$$ |$$$$$$\ $$ |  $$ |$$ |     \$$$$$$  |
\__|      \__|       \______/  \_______|\______|\__|  \__|\__|      \______/ 
 """
class ProdInfo(Screen, BoxLayout, GridLayout):
    '''
    The ProdInfo screen implements the detailed product information screen that shows
    product details such as full product name, price, quantity available, availability, 
    and any extra detail. The product information screen also allows the user to specify
    a quantity of a product to add to their cart, to navigate back to the search screen,
    to view their cart, and to go to the home screen.
    '''
    qtyBuy = ObjectProperty(None) # The quantity of an item the user adds to cart
    item = None # what the user clicked on in the results list
    product = ListProperty([]) # the dicitonary of the item the user clicked
    full_data = ListProperty([])
    my_label = ListProperty([])
    productInfo = {}

    # get the list of all results
    def send_query_results(self, full_data=None, labels=None):
        self.full_data = full_data

    # get the item the user clicked on
    def sendItem(self, item=None):
        self.item = item
        # print(item)
        self.getProduct()

    # get the dict of the item the user clicked on
    def getProduct(self):
        count = 0
        #print(self.full_data)
        # full_data is a list that contains a single entry which is a list
        for lis in self.full_data:
            #pp.pprint(lis)
            # The innermost list contains all the dicts
            for dic in lis:
                #pp.pprint(dic) 
                #print(f'{dic["item"]}, {self.item}')
                # if the "item" entry in the dict matched the item the user
                # clicked on, assign the entire dict to product
                if dic["item"] == self.item and count < 1:
                    pp.pprint(dic)
                    #make the product dict available to other functions
                    self.productInfo = dic
                    # If the dict has more the "details" key
                    if "details" in dic.keys():
                        # Move extra info to the end of the dict
                        dic["alt names"] = f"{dic['details']['name0']}\n{dic['details']['name1']}\n{dic['details']['name2']}"
                        # delete the old dict in the middle
                        del dic["details"]
                    else:
                        dic["alt names"] = f"None"
                    #print(type(dic))
                    
                    # build product dictionary
                    self.product = [ {'text': str(dic['_id'])}, {'text': str(dic['item'])}, {'text': str(dic['quantity'])}, 
                                      {'text': str(dic['availability'])}, {'text': str(dic['price'])}, {'text': str(dic['alt names'])} ]

                    print(self.product)

                    count += 1
    

    def addToCart(self):

        if self.productInfo["availability"] == False:
            # Create a popup window 
            unavailablePopup = Popup(title="Unavailable item", title_align="center", 
                content=Label(text="This item is currently unavailable for purchase"), 
                size_hint=(.75,.5))
            
            # Show the popup
            unavailablePopup.open()

            self.qtyBuy.text = ""

        elif self.qtyBuy.text == "" or int(self.qtyBuy.text) <= 0 or self.qtyBuy.text.isnumeric() == False:
             # Create a popup window 
            amountPopup = Popup(title="Invalid Amount", title_align="center", 
                content=Label(text="Please enter a valid amount"), 
                size_hint=(.75,.5))
            # Show the popup
            amountPopup.open()

            self.qtyBuy.text = ""
        
        elif int(self.qtyBuy.text) > int(self.productInfo["quantity"]):
            # Create a popup window 
            stockPopup = Popup(title="Not enough in stock", title_align="center", 
                content=Label(text=f"There is not enough product in stock.\
                    \n{self.productInfo['quantity']} is the maximum limit."), 
                size_hint=(.75,.5))
            # Show the popup
            stockPopup.open()

            self.qtyBuy.text = f"{self.productInfo['quantity']}"

        else:
            # This info is for the customer and checkout
            global shopCartInfo 
            shopCartInfo.append({"item": self.productInfo['item'], "qty":int(self.qtyBuy.text), "price":round((int(self.qtyBuy.text) * self.productInfo["price"]),2)}) ############################################ ADD PRICE TO THIS LATER

            # This info is for updating the database
            dbInfo.append({"id": self.productInfo['_id'], "qty":int(self.qtyBuy.text)})

             # Create a popup window 
            amountPopup = Popup(title="Added to cart", title_align="center", 
                content=Label(text=f"{self.qtyBuy.text} {self.productInfo['item']} added to your cart"), size_hint=(.75,.5))
            # Show the popup
            amountPopup.open()

            self.qtyBuy.text = ""

    def clear_qty_box(self):
        self.qtyBuy.text = ""
        
"""
$$$$$$$\                            $$\ $$\    $$\ $$\                         
$$  __$$\                           $$ |$$ |   $$ |\__|                        
$$ |  $$ | $$$$$$\   $$$$$$\   $$$$$$$ |$$ |   $$ |$$\  $$$$$$\  $$\  $$\  $$\ 
$$$$$$$  |$$  __$$\ $$  __$$\ $$  __$$ |\$$\  $$  |$$ |$$  __$$\ $$ | $$ | $$ |
$$  ____/ $$ |  \__|$$ /  $$ |$$ /  $$ | \$$\$$  / $$ |$$$$$$$$ |$$ | $$ | $$ |
$$ |      $$ |      $$ |  $$ |$$ |  $$ |  \$$$  /  $$ |$$   ____|$$ | $$ | $$ |
$$ |      $$ |      \$$$$$$  |\$$$$$$$ |   \$  /   $$ |\$$$$$$$\ \$$$$$\$$$$  |
\__|      \__|       \______/  \_______|    \_/    \__| \_______| \_____\____/                                                                                                                                                                                                                                       
"""

class ProdView(RecycleDataViewBehavior, Button):
    '''
    The ProdView class implements the recycleview used to display detailed product
    information. All information is presented as non-clickable buttons. The majority
    of the ProdView class behavior is defined in the ProdView class in the .kv file
    '''
    def refresh_view_attrs(self, rec_view, my_index, data):
        self.my_index = my_index
        return super(ProdView, self).refresh_view_attrs(rec_view, my_index, data)

    def apply_selection(self, rec_view, my_index, am_selected): 
        self.selected = am_selected

"""
 $$$$$$\  $$\                                     $$\                      $$$$$$\                       $$\     
$$  __$$\ $$ |                                    \__|                    $$  __$$\                      $$ |    
$$ /  \__|$$$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  $$\ $$$$$$$\   $$$$$$\  $$ /  \__| $$$$$$\   $$$$$$\ $$$$$$\   
\$$$$$$\  $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$ |$$  __$$\ $$  __$$\ $$ |       \____$$\ $$  __$$\\_$$  _|  
 \____$$\ $$ |  $$ |$$ /  $$ |$$ /  $$ |$$ /  $$ |$$ |$$ |  $$ |$$ /  $$ |$$ |       $$$$$$$ |$$ |  \__| $$ |    
$$\   $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |$$ |  $$\ $$  __$$ |$$ |       $$ |$$\ 
\$$$$$$  |$$ |  $$ |\$$$$$$  |$$$$$$$  |$$$$$$$  |$$ |$$ |  $$ |\$$$$$$$ |\$$$$$$  |\$$$$$$$ |$$ |       \$$$$  |
 \______/ \__|  \__| \______/ $$  ____/ $$  ____/ \__|\__|  \__| \____$$ | \______/  \_______|\__|        \____/ 
                              $$ |      $$ |                    $$\   $$ |                                       
                              $$ |      $$ |                    \$$$$$$  |                                       
                              \__|      \__|                     \______/                                       
"""
class ShoppingCart(Screen,BoxLayout,GridLayout):
    '''
    The ShoppingCart class implements the shopping cart screen, which shows all
    items in a user's cart, along with quantity of that item in the cart and
    the price. 
    '''
    items = ListProperty()
    qty = ListProperty()
    price = ListProperty()
    totalPrint = StringProperty("0.00")

    # The screen updates itself as soon as the user enters
    def on_pre_enter(self):
        total = 0.00
        global shopCartInfo
        itemList = shopCartInfo
        #print(itemList)
        for item in itemList:
            #print(item)
            #print(type(item))
            self.items.append({'text': str(item['item'])})
            self.qty.append({'text': str(item['qty'])})
            self.price.append({'text':str(item['price'])})
        shopCartInfo.clear()

        # Adds up all prices in the list
        for dic in self.price:
            total += (float(dic['text']))
        
        # Only print two decimal places
        TWO = decimal.Decimal(10) ** -2
        total = decimal.Decimal(total).quantize(TWO)
        self.totalPrint = f"{total}"

    # The clear_recview method resets all items, quantity, and associated prices 
    # in the recycleview for the shopping cart. This is called upon checkout and logout.
    def clear_recview(self):
        cartToClear = wm.get_screen("shoppingCart")
        cartToClear.items = []
        cartToClear.qty = []
        cartToClear.price = []

    # exitInno resets all shopping cart information on the python side (not the .kv 
    # recycleview implementation)
    def exitInno(self, instance):
        global shopCartInfo
        self.totalPrint = "0.00"
        shopCartInfo.clear()

        self.clear_recview()

        wm.current = "homepage"

    # The checkout method prompts the user to confirm they wish to checkout. If yes is selected,
    # the purchase is made. If no is selected, the user is returned to their shopping cart.
    def checkout(self,):
        window = BoxLayout(orientation="vertical")
        window.add_widget(Label(text = "Are you sure you want to checkout?"))
        popup = Popup(title="Check out?", size_hint = (.75,.5), content = window)
        window.add_widget(Button(text = "Yes", on_press = popup.dismiss, on_release = self.exitInno))
        window.add_widget(Button(text = "No", on_press = popup.dismiss))
        popup.open()

    
"""
 $$$$$$\                       $$\   $$\    $$\ $$\                         
$$  __$$\                      $$ |  $$ |   $$ |\__|                        
$$ /  \__| $$$$$$\   $$$$$$\ $$$$$$\ $$ |   $$ |$$\  $$$$$$\  $$\  $$\  $$\ 
$$ |       \____$$\ $$  __$$\\_$$  _|\$$\  $$  |$$ |$$  __$$\ $$ | $$ | $$ |
$$ |       $$$$$$$ |$$ |  \__| $$ |   \$$\$$  / $$ |$$$$$$$$ |$$ | $$ | $$ |
$$ |  $$\ $$  __$$ |$$ |       $$ |$$\ \$$$  /  $$ |$$   ____|$$ | $$ | $$ |
\$$$$$$  |\$$$$$$$ |$$ |       \$$$$  | \$  /   $$ |\$$$$$$$\ \$$$$$\$$$$  |
 \______/  \_______|\__|        \____/   \_/    \__| \_______| \_____\____/ 
 """
class CartView(RecycleDataViewBehavior, Button):
    '''
    The CartView class implements the recycleview used by the ShoppingCart class.
    The vast majority of CartView is implemented in the CartView class in the .kv file.
    CartView utilizes three separate recycleviews to show item names, quantity, and price,
    respectively.
    '''
    def refresh_view_attrs(self, rec_view, my_index, data):
        self.my_index = my_index
        return super(CartView, self).refresh_view_attrs(rec_view, my_index, data)

    def apply_selection(self, rec_view, my_index, am_selected): 
        self.selected = am_selected


'''
$$$$$$$$\                    $$\     $$$$$$$\              $$\     $$\                         
\__$$  __|                   $$ |    $$  __$$\             $$ |    $$ |                        
   $$ | $$$$$$\   $$$$$$$\ $$$$$$\   $$ |  $$ |$$\   $$\ $$$$$$\ $$$$$$\    $$$$$$\  $$$$$$$\  
   $$ |$$  __$$\ $$  _____|\_$$  _|  $$$$$$$\ |$$ |  $$ |\_$$  _|\_$$  _|  $$  __$$\ $$  __$$\ 
   $$ |$$$$$$$$ |\$$$$$$\    $$ |    $$  __$$\ $$ |  $$ |  $$ |    $$ |    $$ /  $$ |$$ |  $$ |
   $$ |$$   ____| \____$$\   $$ |$$\ $$ |  $$ |$$ |  $$ |  $$ |$$\ $$ |$$\ $$ |  $$ |$$ |  $$ |
   $$ |\$$$$$$$\ $$$$$$$  |  \$$$$  |$$$$$$$  |\$$$$$$  |  \$$$$  |\$$$$  |\$$$$$$  |$$ |  $$ |
   \__| \_______|\_______/    \____/ \_______/  \______/    \____/  \____/  \______/ \__|  \__|                                                                                                                                                                                                                                                                                      
'''
class TestButton(Screen):
    ''' 
    The TestButton class is used to test a specific button functionality on a kivy screen.
    This may be useful for observing the behavior of a method bound to a button press.
    '''
    # If text input is needed, use test_input
    test_input = ObjectProperty(None)

    def testSearch(self):
        wm.current = "searchView"

'''
 $$$$$$\             $$\                         
$$  __$$\            $$ |                        
$$ /  \__| $$$$$$\ $$$$$$\   $$\   $$\  $$$$$$\  
\$$$$$$\  $$  __$$\\_$$  _|  $$ |  $$ |$$  __$$\ 
 \____$$\ $$$$$$$$ | $$ |    $$ |  $$ |$$ /  $$ |
$$\   $$ |$$   ____| $$ |$$\ $$ |  $$ |$$ |  $$ |
\$$$$$$  |\$$$$$$$\  \$$$$  |\$$$$$$  |$$$$$$$  |
 \______/  \_______|  \____/  \______/ $$  ____/ 
                                       $$ |      
                                       $$ |      
                                       \__|      
'''                                                                    
# Load the kv language file that supplements this python script
# Much of the functionality of this app is intertwined with the kv lang script                                    
kv = Builder.load_file("Innoventory.kv")

# Get a window manager object to switch between screens
wm = WindowManager()

# A list of screens - each is a class that inherits from the Screen class in kivy.uix.screenmanager
screens = [Login(name="login"), CreateAccount(name="createAcct"), Homepage(name="homepage"), 
            SettingsMenu(name="settingsMenu"), ChangePassword(name="changePassword"),
             TestButton(name='testButton'), ProdInfo(name="prodInfo"), SearchView(name="searchView"),
             ShoppingCart(name="shoppingCart")]

# Add each screen widget to the window manager
for screen in screens:
    wm.add_widget(screen)

# Set the first screen the user will see when the app is launched
# By default, the first screen is the login screen
wm.current = "login"

# Build the main app
# If main().run() is called from main, the full app will be launched
class main(App):
    title = "Innoventory"

    def build(self):
        return wm

# Build a test app
# If TestApp().run() is called from main, a subset of functionality is being tested
class TestApp(App):
    title = "Search Functionality Test"

    def build(self):
        return SearchView()

'''
$$\      $$\           $$\           
$$$\    $$$ |          \__|          
$$$$\  $$$$ | $$$$$$\  $$\ $$$$$$$\  
$$\$$\$$ $$ | \____$$\ $$ |$$  __$$\ 
$$ \$$$  $$ | $$$$$$$ |$$ |$$ |  $$ |
$$ |\$  /$$ |$$  __$$ |$$ |$$ |  $$ |
$$ | \_/ $$ |\$$$$$$$ |$$ |$$ |  $$ |
\__|     \__| \_______|\__|\__|  \__|                                                                                                        
'''
if __name__ == "__main__":

    main().run()
    #TestApp().run()
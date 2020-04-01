
import pymongo
import urllib.parse
import pprint
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors import ButtonBehavior  
from kivy.uix.widget import Widget
from kivy.uix.button import Button
import api

pp = pprint.PrettyPrinter(indent=4)
username = ""

############################### UNCOMMENT TO SKIP LOGIN ########################

# class Login(Screen):
#     username = "passwordHell"
#     password = r"XR9lYeOp036C%25%40%26%40cQn%2A8z3BU4%5C"
#     global client, db, collections
#     client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@innoventory-vvoxp.azure.mongodb.net/test?retryWrites=true&w=majority")
#     db = client.Innoventory
#     collections = db.list_collection_names()
#     print("Connected")

#     def login(self):
#         wm.current="homepage"

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

class Hell(Screen):
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

    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def login(self):
        # Get an instance of the login class from the api
        login = api.Login()

        global username  # made this global on line 22
        
        self.username =  urllib.parse.quote(self.usernameIn.text) # passwordHell
        self.password =  urllib.parse.quote(self.passwordIn.text) # XR9lYeOp036C%@&@cQn*8z3BU4\

        username = self.username
        
        try:
            # Will return a dictionary of user information. If the username and/or password
            # are wrong, an emtpy username and password are returned
            result, _ = login.login({'username': self.username, 'password': self.password})
            
            if(result['username'] != "" and result['password'] != ""):
                # If the login is successful, take the user to the homepage window
                wm.current = "homepage"
            else:
                # Create a popup window to display the authentication failure
                invalidLoginPopup = Popup(title="Authentication Failure", title_align="center", 
                    content=Label(text="Login Failed"), size_hint=(None, None), size=(250,250))
                
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
    searchPhrase = ObjectProperty(None)
       
    def logout(self):
        wm.current = "login"
    
    def settingsMenu(self):
        wm.current = "settingsMenu"

    def search(self): ###################################################   DOESN'T WORK #####
        
        if(self.searchPhraseIn.text != ""):
            self.searchPhrase = self.searchPhraseIn.text
            print(self.searchPhrase)
            self.searchPhraseIn.text = ""
    #     else:
    #         # Create a popup window to display the authentication failure
    #         emptySearchPopup = Popup(title="Invalid Search", title_align="center", 
    #             content=Label(text="Search cannot be empty"), size_hint=(None, None), size=(250,250))
    #         emptySearchPopup.open()

    #     results = []
    #     #look in every collection in the db
    #     for collection in collections:
    #         print(collection)
    #         #search each collection for a match

    #     """https://docs.mongodb.com/manual/text-search/index.html"""
    #     #     results.append(db.collection.find({$text: {$search: self.searchPhrase}}))
    #     # print(results)
    #     #     results.append(db.Vehicles.find({"$text": {"$search": "Honda"}}))
    #     # print(results)

    # def catSearch(self,cat): #cat is an index
    #     collection = collections[cat]
    #     items = db[collection].find({})
    #     for item in items:
    #         pp.pprint(item)
        


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
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def createAccount(self):
        self.username =  urllib.parse.quote(self.usernameIn.text)
        self.password =  urllib.parse.quote(self.passwordIn.text)

        # Get a UserManager object
        user = api.UserManager()
        # Create the user
        # Returns True if the user was successfully created
        result = user.createUser({'username': self.username, 'password': self.password})

        if result == True:
            print("Successfully created user")
            wm.current = "homepage"
        else:
            # Create a popup window to display the authentication failure
            failedUserCreationPopup = Popup(title="User Creation Failure", title_align="center", 
                content=Label(text="User Creation Failed\n Username Taken"), size_hint=(None, None), size=(250,250))
                
            # Show the authentication failure popup
            failedUserCreationPopup.open()

        self.reset()

    # Removes input from text boxes
    def reset(self):
        self.usernameIn.text = ""
        self.passwordIn.text = ""

"""
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
"""
class SettingsMenu(Screen):
    def changePassword(self):
        wm.current = "changePassword"



"""
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
# """
class ChangePassword(Screen,):
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
                content=Label(text="Password Changed!"), size_hint=(None, None), size=(250,250))
            passChangePopup.open()
        
        else:
            print("password change fail")
   
    # Removes input from text boxes
    def reset(self):
        self.oldPasswordIn.text = ""
        self.newPasswordIn.text = ""
        self.newPasswordIn2.text = ""


"""
$$\      $$\ $$\                     
$$$\    $$$ |\__|                    
$$$$\  $$$$ |$$\  $$$$$$$\  $$$$$$$\ 
$$\$$\$$ $$ |$$ |$$  _____|$$  _____|
$$ \$$$  $$ |$$ |\$$$$$$\  $$ /      
$$ |\$  /$$ |$$ | \____$$\ $$ |      
$$ | \_/ $$ |$$ |$$$$$$$  |\$$$$$$$\ 
\__|     \__|\__|\_______/  \_______|
"""                                                                    
                                     
kv = Builder.load_file("Innoventory.kv")

wm = WindowManager()
screens = [Login(name="login"), CreateAccount(name="createAcct"), Homepage(name="homepage"), 
            SettingsMenu(name="settingsMenu"), ChangePassword(name="changePassword"), Hell(name='hell')]
for screen in screens:
    wm.add_widget(screen)

wm.current = "login"  #default login
class main(App):
    def build(self):
        return wm


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
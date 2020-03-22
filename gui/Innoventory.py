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

pp = pprint.PrettyPrinter(indent=4)

client=""
db=""
collections=[]
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


class Login(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)


    
    def login(self):
        self.username =  urllib.parse.quote(self.usernameIn.text) # passwordHell
        self.password =  urllib.parse.quote(self.passwordIn.text) # XR9lYeOp036C%@&@cQn*8z3BU4\


        try:
            global client, db, collections
            client = pymongo.MongoClient(f"mongodb+srv://{self.username}:{self.password}@innoventory-vvoxp.azure.mongodb.net/test?retryWrites=true&w=majority")
            db = client.Innoventory
            collections = db.list_collection_names()
            print("Connected")   
            wm.current = "homepage"
            self.reset()

        except pymongo.errors.OperationFailure or pymongo.errors.InvalidURI:
            print("ruh-roh")
            self.reset()

    #Removes input from text boxes
    def reset(self):
        self.usernameIn.text = ""
        self.passwordIn.text = ""
        
    #Do we need to create accounts if only superuser can add people?
    #Can you even make an account without signing up on atlas?
    def createAcct(self):
        wm.current = "createAcct"


class Homepage(Screen):
    searchPhrase = ObjectProperty(None)

    def search(self): ###################################################   DOESN'T WORK #####
        self.searchPhrase = self.searchPhraseIn.text
        print(self.searchPhrase)
        results = []
        #look in every collection in the db
        for collection in collections:
            print(collection)
            #search each collection for a match

        """https://docs.mongodb.com/manual/text-search/index.html"""
        #     results.append(db.collection.find({$text: {$search: self.searchPhrase}}))
        # print(results)
        #     results.append(db.Vehicles.find({"$text": {"$search": "Honda"}}))
        # print(results)





    def catSearch(self,cat): #cat is an index
        collection = collections[cat]
        items = db[collection].find({})
        for item in items:
            pp.pprint(item)
        


class CreateAccount(Screen):
    pass



kv = Builder.load_file("Innoventory.kv")

wm = WindowManager()
screens = [Login(name="login"), CreateAccount(name="createAcct"), Homepage(name="homepage")]
for screen in screens:
    wm.add_widget(screen)

wm.current = "login"  #default login
class main(App):
    def build(self):
        return wm



if __name__ == "__main__":
    main().run()
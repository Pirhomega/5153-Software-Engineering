#!/usr/bin/env python3

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from pprint import pprint

from api import Login


class InnoventoryLogin(Widget):
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def buttonPress(self):
        testString = "Username: " + self.username.text + " Password: " + self.password.text
        print(testString)

        # On button press, create a login object
        authenticate = Login()
        # Check to see if the user and password are valid
        userInfo = authenticate.login({'username': self.username.text, 'password': self.password.text})
        # If the user/password combination was valid, the pprint command will print the user's information
        # If the user/password combination was not valid, the userInfo object will print empty strings
        pprint(userInfo)

        # Clear text from input boxes
        self.username.text = ""
        self.password.text = ""



class InnoventoryApp(App):
    def build(self):
        return InnoventoryLogin()


if __name__ == "__main__":
        InnoventoryApp().run()
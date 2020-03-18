#!/usr/bin/env python3

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class InnoventoryLogin(Widget):
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def buttonPress(self):
        testString = "Username: " + self.username.text + " Password: " + self.password.text
        print(testString)
        self.username.text = ""
        self.password.text = ""



class InnoventoryApp(App):
    def build(self):
        return InnoventoryLogin()


if __name__ == "__main__":
        InnoventoryApp().run()
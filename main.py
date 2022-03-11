__author__ = "HiroYito B"
__version__ = "0.1.0"
__date__ = "2021-03-06"

"""
    This is Mobile App designed to send email using Kivy lib.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from glob import glob
from pathlib import Path
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from models.users import User
import random


Builder.load_file("interface.kv")


class HomeScreen(Screen, User):
    def sign_up(self):
        # get around to fix DBus issue export DBUS_FATAL_WARNINGS=0 unset XMODIFIERS
        self.manager.current = "sign_up_screen"

    def login_check_screen(self, email, password):
        try:
            if self.login(email, password):
                print("passed self.login")
                self.manager.transition.direction = "right"
                self.manager.current = "login_success_screen"
                return
            self.ids.wrong_credentials.text = "Wrong username:email or password"
        except ValueError as ex:
            self.ids.wrong_credentials.text = str(ex)


class SignUpScreen(Screen, User):
    def sign_up_screen(self, email, password):
        try:
            if self.register(email, password):
                print(f"{email} registered!")
                self.manager.current = "sign_up_success_screen"
            else:
                self.ids.user_message.text = f"{email} not registered"
        except ValueError as ex:
            self.ids.user_message.text = str(ex)

    def home_screen(self):
        self.manager.transition.direction = "right"
        self.manager.current = "home_screen"


class SignUpSuccessScreen(Screen):
    def go_to_login_screen(self):
        self.manager.transition.direction = "right"
        self.manager.current = "home_screen"


class LoginSuccessScreen(Screen):
    def logout(self):
        self.manager.transition.direction = "right"
        self.manager.current = "home_screen"

    def quote(self, feeling):
        print("hitting quote method")
        files = glob("quotes/*.txt")
        sentiments = [Path(feeling).stem for feeling in files]
        if feeling in sentiments:
            with open(f"quotes/{feeling}.txt") as file:
                quotes = file.readlines()
            self.ids.message.text = random.choice(quotes)
        else:
            self.ids.message.text = "Unfortunately this quote is out of scope"


class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self) -> RootWidget:
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()

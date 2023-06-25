import webbrowser

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty, OptionProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRoundFlatButton, MDFlatButton, MDRoundFlatIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField


class Background(Widget):
    pass


class MyLayout(FloatLayout):
    screen_mngr = ObjectProperty(None)


class BoxLayout1(MDBoxLayout):
    pass


class LoginScreen(Screen):
    pass


class RegisterScreen(Screen):
    pass


class FgtPasswordScreen(Screen):
    pass


class Form(MDBoxLayout):
    pass


class CommonComponentLabel(MDLabel):
    pass


class MDTextFieldFullName(MDTextField):
    pass


class MDTextFieldEmail(MDTextField):
    pass


class MDTextFieldPassword(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()


class MDTextFieldConfirmPassword(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()


class LoginButton(MDRoundFlatButton, HoverBehavior):
    def on_enter(self, *args):
        self.md_bg_color = "#BEAFC2"
        self.text_color = "white"

    def on_leave(self, *args):
        self.md_bg_color = "1F6E8C"
        self.text_color = "white"


class RegisterButton(MDRoundFlatButton, HoverBehavior):
    def on_enter(self, *args):
        self.md_bg_color = "#BEAFC2"
        self.text_color = "white"

    def on_leave(self, *args):
        self.md_bg_color = "white"
        self.text_color = "#BB86FC"


class ForgetPassword(MDFlatButton, HoverBehavior):
    def on_enter(self, *args):
        self.text_color = "E8A0BF"

    def on_leave(self, *args):
        self.text_color = "0C134F"


class LoginWith(MDRoundFlatIconButton, HoverBehavior):
    def on_enter(self, *args):
        self.md_bg_color = "#BEAFC2"
        self.text_color = "white"

    def on_leave(self, *args):
        self.md_bg_color = "C2DEDC"
        self.text_color = "black"

    def google(self):
        webbrowser.open("https://accounts.google.com/")

    def facebook(self):
        webbrowser.open("https://m.facebook.com/login/?locale=en_GB")


class MobileView(MDScreen):
    pass


class TabletView(MDScreen):
    pass


class DesktopView(MDScreen):
    pass


class ResponsiveView(MDResponsiveLayout, MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.mobile_view = MobileView()
        self.tablet_view = TabletView()
        self.desktop_view = DesktopView()


class MainApp(MDApp):
    media = OptionProperty('M', options=('XS', 'S', 'M', 'L', 'XL'))

    def build(self):
        Window.bind(size=self.update_media)
        return Builder.load_file('MainApp.kv')

    def update_media(self, win, size):
        width, height = size
        self.media = (
            'XS' if width < 250 else
            'S' if width < 500 else
            'M' if width < 1000 else
            'L' if width < 1200 else
            'XL'
        )

    def on_checkbox_active(self, checkbox, value):
        if value:
            print('The checkbox', checkbox, 'is active', 'and', checkbox.state, 'state')
        else:
            print('The checkbox', checkbox, 'is inactive', 'and', checkbox.state, 'state')

    # def on_start(self):
    #     self.fps_monitor_start()


if __name__ == "__main__":
    MainApp().run()

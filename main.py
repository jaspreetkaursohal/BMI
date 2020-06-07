import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class FirstWindow(Screen):
    pass


class SecondWindow(Screen):
    def calc(self, _height, weight):
        w = float(weight.text)
        h = float(_height.text)
        BMI = round(((w * 0.453592) / pow((h * 0.0254), 2)))
        print(BMI)



class ThirdWindow(Screen):
    def calc(self, _height, weight):
        w = float(weight.text)
        h = float(_height.text)
        BMI = round(w / pow(h, 2))
        print(BMI)


class FourthWindow(Screen):
    pass


class WindowsManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MyApp(App):

    def build(self):
        return kv


if __name__ == '__main__':
    MyApp().run()

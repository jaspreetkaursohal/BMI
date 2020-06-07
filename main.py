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
        BMI =((w * 0.453592) / pow((h * 0.0254), 2))
        print('Your BMI is',BMI)
        if BMI<18.5:
            print("Under weight")
        if BMI>=18.5 and BMI<=24.9:
            print("Normal weight ")
        if BMI>=25.0 and BMI<=29.9:
            print("Pre-obesity")
        if BMI>=30.0 and BMI<=34.9:
            print("Obesity class I")
        if BMI>=35.0 and BMI<=39.9:
            print("Obesity class II")
        if BMI>40:
            print("Obesity class III")


class ThirdWindow(Screen):
    def calc(self, _height, weight):
        w = float(weight.text)
        h = float(_height.text)
        BMI = w / pow(h, 2)

        print('Your BMI is',BMI)
        if BMI<18.5:
            print("Under weight")
        if BMI>=18.5 and BMI<=24.9:
            print("Normal weight ")
        if BMI>=25.0 and BMI<=29.9:
            print("Pre-obesity")
        if BMI>=30.0 and BMI<=34.9:
            print("Obesity class I")
        if BMI>=35.0 and BMI<=39.9:
            print("Obesity class II")
        if BMI>40:
            print("Obesity class III")

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

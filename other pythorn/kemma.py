import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require('1.11.1')


class Kemmasoft(App):
    def build(self):
        return Label(text="Kemmasoft")


if __name__ == '__main__':
    Kemmasoft().run()
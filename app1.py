from kivy.app import App
from kivy.uix.label import Label

#base class
class myapp(App):
    def build(self):
        return Label(text='Daniel Chacha Application ')


if __name__ == '__main__':
    myapp().run()
        
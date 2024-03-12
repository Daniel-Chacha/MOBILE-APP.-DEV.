#program to make a checkbox in kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.checkbox import CheckBox

class demoapp(GridLayout):
    def __init__(self,**kwargs):
        super(demoapp,self).__init__(**kwargs)

        self.cols=2

        self.add_widget(Label(text='Male'))
        self.active=CheckBox(active=True)
        self.add_widget(self.active)

        self.add_widget(Label(text='Female'))
        self.active=CheckBox(active=True)
        self.add_widget(self.active)

        self.add_widget(Label(text='Others'))
        self.active=CheckBox(active=True)
        self.add_widget(self.active)

class checkboxapp(App):
    def build(self):
        return demoapp()
    
if __name__=='__main__':
    checkboxapp().run()
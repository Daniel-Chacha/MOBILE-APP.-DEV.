#create a login interface
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


#create a class used as a base for the root widget for the loginscreen
class loginscreen(GridLayout):
    #overriding the method '__init__' so as to add widgets and define their behaviour
    def __init__(self,**kwargs):
        super(loginscreen,self).__init__(**kwargs)

        self.cols=2                                         #gridlayout managing its children in two columns and add a label anmd textinput for email id and password
        self.add_widget(Label(text='Email ID'))
        self.username=TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='Password'))
        self.password=TextInput(password=True,multiline=False)
        self.add_widget(self.password)

class myapp(App):
    def build(self):
        return loginscreen()
    
    
if __name__ =='__main__':
    myapp().run()
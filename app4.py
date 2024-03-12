from kivymd.app import MDApp
from kivymd.uix.button import MDFloatingActionButton,MDFlatButton
from kivymd.uix.screen import Screen
from kivymd.icon_definitions import md_icons

class demoapp(MDApp):
    def build(self):
        screen=Screen()
        btn1=MDFlatButton(text='Hello World!',pos_hint={'center_x':0.5,'center_y':0.8})
        btn2=MDFloatingActionButton(icon='apple', pos_hint={'center_x':0.5,'center_y':0.5})
        
        screen.add_widget(btn1)
        screen.add_widget(btn2)

        return screen
    
demoapp().run()
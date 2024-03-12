from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp #another way to run kivy app


dropdown=DropDown()
for x in range(10):
    btn=Button(text='Value %d' %x,size_hint_y=None,height=40)
    btn.bind(on_release=lambda btn:dropdown.select(btn.text))   #binding the button to show text when selected
    dropdown.add_widget(btn)    


mainbutton=Button(text='Hello',size_hint=(None,None),pos=(350,400))

#show the dropdown menu when mainbutton is released
mainbutton.bind(on_release=dropdown.open)

#listen for the selection in the dropdown list and assign the data to the button text
dropdown.bind(on_select=lambda instance,x :setattr(mainbutton,'text',x))


runTouchApp(mainbutton)
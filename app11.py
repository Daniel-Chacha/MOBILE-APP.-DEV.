#window size adjustments using kivy.config
#should be imported before any other module

from kivy.config import Config
Config.set('graphics','resizable','True')     #'1' is used to indicate "true" or "resizable", and '0' is used to indicate "false" or "not resizable".

from kivy.app import App
from kivy.uix.label import Label

class mydemoapp(App):
    def build(self):
        l=Label(text='[color=ff3333][i]Hello!![/i][/color]\n [color=3333ff]World![/color]',font_size='20sp',markup=True)
        return l
    
mydemoapp().run()


# either the height or width or both can be set

Config.set('graphics','resizable','0')
Config.set('graphics','width','500')
Config.set('graphics','height','500')

class newdemoapp(mydemoapp):
    pass
newdemoapp().run()
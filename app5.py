from kivy.app import App
from kivy.uix.label import Label

class mylabelapp(App):
    def build(self):
        lbl=Label(text='Label is added onto the screen!!:')
        return lbl
mylabelapp().run()


#styling a label
class mylabelap2(App):
    def build(self):
        lbl=Label(text='Label is added on \nto the screen and it\n is multiline',font_size='20sp',color=(0.41,0.42,0.72,1))
        return lbl    #the color is set to RGBA =RED, GREEN , BLUE, ALPHA
mylabelap2().run()


#markup the text with different colors
class mylabelapp3(App):
    def build(self):
        lbl=Label(text="[color=ff3333][b]'Label'[/b] is added [/color]\n [color=3333ff]screen!![/color] ",font_size='20sp',markup=True)
        return lbl

mylabelapp3().run()



#[b][/b] -> Activate bold text
#[i][/i] -> Activate italic text
#[u][/u] -> Underlined text
#[s][/s] -> Strikethrough text
#[font=][/font] -> Change the font
#[size=][/size]] -> Change the font size
#[color=#][/color] -> Change the text color
#[ref=][/ref] -> Add an interactive zone. The reference + bounding box inside the reference will be available in Label.refs
#[anchor=] -> Put an anchor in the text. You can get the position of your anchor within the text with Label.anchors
#[sub][/sub] -> Display the text at a subscript position relative to the text before it.
#[sup][/sup] -> Display the text at a superscript position relative to the text before it.
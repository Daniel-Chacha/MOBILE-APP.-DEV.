from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen

class demo(MDApp):
    def build(self):
        s=Screen()

        l1=MDLabel(text='Welcome', pos_hint={'center_x':0.8,'center_y':0.8},theme_text_color='Primary',text_color=(0.5,0,0.5,1),font_style='H3')
        l2=MDLabel(text='Welcome',pos_hint={'center_x':0.8,'center_y':0.5},theme_text_color='Primary',text_color=(0.5,0,0.5,1),font_style='H2')
        l3=MDLabel(text='Welcome',pos_hint={'center_x':0.8,'center_y':0.2},theme_text_color='Primary',text_color=(0.5,0,0.5,1),font_style='H1')

        s.add_widget(l1)
        s.add_widget(l2)
        s.add_widget(l3)

        return s
    
if __name__ =="__main__":
    demo().run()
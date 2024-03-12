#create a checkbox and add a callback
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox

class check_box(GridLayout):
    def __init__(self,**kwargs):
        super(check_box,self).__init__(**kwargs)

        self.cols=2

        self.add_widget(Label(text='Male'))
        self.active=CheckBox(active=True)
        self.add_widget(self.active)

        self.lbl_active=Label(text='Checkbox is on')   #adding label to screen
        self.add_widget(self.lbl_active)

        #attaching a callback
        self.active.bind(active=self.on_checkbox_active)

        #callback for the checkbox
        def on_checkbox_active(self, demoappInstance,isActive):
            if isActive:
                self.lbl_active.text='Checkbox is ON'
                print('Checkbox Checked')
            else:
                self.lbl_active.text='Checkbox is OFF'
                print('Checkbox unchecked')

class checkboxapp(App):
    def build(self):
        return check_box()
    
if __name__=='__main__':
    checkboxapp().run()
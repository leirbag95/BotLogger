from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class MyGrid(Widget):
    pass
    # def __init__(self, **kwargs):
    #     super(MyGrid, self).__init__(**kwargs)
    #     self.cols = 3
    #     self.add_widget(Label(text="Name: "))
    #     self.name = TextInput(multiline=False)
    #     self.add_widget(self.name)
    #     self.record = Button(text="Record")
    #     # set button function
    #     self.record.bind(on_press=self.pressed)
    #     self.add_widget(self.record)
    
    # def pressed(self, instance):
    #     print("enter")

class MyApp(App):
    def build(self):
        return MyGrid()

    
if __name__ == "__main__":
    MyApp().run()
    pass
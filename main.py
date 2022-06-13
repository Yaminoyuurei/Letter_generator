from kivy.config import Config
Config.set('graphics', 'width', '1280')
Config.set('graphics', 'height', '720')
from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout

class MainMenu(GridLayout):
    pass

class Lettre(App):
    manager = ObjectProperty(None)

    def build(self):
        self.manager = MainMenu()
        return self.manager
    
Lettre().run()

from kivy.config import Config
import json
import os.path
from module.Lettre import Letter
from module.Person import Person
from kivy.core.window import Window 
from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel

Window.clearcolor = (0, 0, 0, 1) 
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
# Config.set('graphics','resizable',0)

class MainMenu(GridLayout):
    
    def __init__(self,**kwargs,):
        self.dest = Person()
        self.letter = Letter()
        if os.path.isfile("data.json"):
            f = open('data.json', 'r')
            data_json = f.read()
            data = json.loads(data_json) 
            f.close()     
            self.exp = Person(data['nom'],data['prenom'],data['adresse'],data['cp'],data['ville'],data['tel'],data['mail'])    
        else:
            self.exp = Person()
        super().__init__(**kwargs)
    
    def reinit(self):
        self.exp = Person()
        self.dest = Person()
        self.obj = ""
        self.msg = ""
        
    def associate(self,input):
        # Mise à jour de l'expéditeur
        self.exp.nom = input[0][0]
        self.exp.prenom = input[0][1]
        self.exp.adresse = input[0][2]
        self.exp.cp = input[0][3]
        self.exp.ville = input[0][4]
        self.exp.tel = input[0][5]
        self.exp.mail = input[0][6]
        # Mise à jour du destinataire
        self.dest.nom = input[1][0]
        self.dest.prenom = input[1][1]
        self.dest.adresse = input[1][2]
        self.dest.cp = input[1][3]
        self.dest.ville = input[1][4]
        # Mise à jour du Message
        self.obj = input[2][1]
        self.msg = input[2][0]
        
        
    def create_letter(self,input):
        self.associate(input)
        is_okay = self.letter.save_letter(self.exp,self.dest,self.obj,self.msg)
        if is_okay:
            self.show_dialog("Lettre créée avec succès")
        else:
            self.show_dialog("Erreur lors de la création de la lettre",True)
           
    def create_json(self,input):
        self.associate(input,True)
        exp_json = {'nom':self.exp.nom,
                    'prenom':self.exp.prenom,
                    'adresse':self.exp.adresse,
                    'cp':self.exp.cp,
                    'ville':self.exp.ville,
                    'tel':self.exp.tel,
                    'mail':self.exp.mail
                    }
        try:
            f= open("data.json","w")
            json.dump(exp_json,f)
            self.show_dialog("Le JSON a été créé")
            f.close()
        except:
            self.show_dialog("Erreur lors de la création du JSON",True)
        
    def show_dialog(self,message,error=False):
        layout = GridLayout(cols=1, padding = 10)
        
        popup_label = Label(text=message)
        layout.add_widget(popup_label)
         
        if error:
            closeButton = Button(text='OK', size_hint_y=None, height=40)
            layout.add_widget(closeButton)
            popup = Popup(title='ERREUR',
                        background_color=(0,0,0,0.5),
                        auto_dismiss=True,
                        content=layout,
                        size_hint=(None, None), 
                        size=(400, 200))
            popup.open()
            closeButton.bind(on_press = popup.dismiss)
        else :
            popup = Popup(title='Information',
                        background_color=(0,0,0,0.5),
                        auto_dismiss=True,
                        content=layout,
                        size_hint=(None, None), 
                        size=(400, 200))
            popup.open()
            Clock.schedule_once(popup.dismiss, 1)

class OldMenu(GridLayout):
    pass

class LetterGenerator(App):
    manager = ObjectProperty(None)

    def build(self):
        self.manager = MainMenu()
        return self.manager
    
LetterGenerator().run()

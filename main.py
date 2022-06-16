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
        self.destinataire = Person()
        self.letter = Letter()
        if os.path.isfile("data/settings.json"):
            f = open('data/settings.json', 'r')
            data_json = f.read()
            data = json.loads(data_json) 
            data_e = data.get('expediteur')
            f.close()     
            self.expediteur = Person(data_e['nom'],
                                     data_e['prenom'],
                                     data_e['adresse'],
                                     data_e['cp'],
                                     data_e['ville'],
                                     data_e['tel'],
                                     data_e['mail'])    
        else:
            self.expediteur = Person()
        super().__init__(**kwargs)
    
    def reinit(self):
        self.expediteur = Person()
        self.destinataire = Person()
        self.obj = ""
        self.msg = ""
    
    def test(self):
        print(self.ids.e_nom.text)   
    
    def associate(self):
        # Mise à jour de l'expéditeur
        self.expediteur.nom = self.ids.e_nom.text
        self.expediteur.prenom = self.ids.e_prenom.text
        self.expediteur.adresse = self.ids.e_adresse.text
        self.expediteur.cp = self.ids.e_cp.text
        self.expediteur.ville = self.ids.e_ville.text
        self.expediteur.tel = self.ids.e_tel.text
        self.expediteur.mail = self.ids.e_mail.text
        # Mise à jour du destinataire
        self.destinataire.nom = self.ids.d_nom.text
        self.destinataire.prenom = self.ids.d_prenom.text
        self.destinataire.adresse = self.ids.d_adresse.text
        self.destinataire.cp = self.ids.d_cp.text
        self.destinataire.ville = self.ids.d_ville.text
        # Mise à jour du Message
        self.obj = self.ids.m_obj.text
        self.msg = self.ids.msg.text
        
        
    def create_letter(self):
        self.associate()
        is_okay = self.letter.save_letter(self.expediteur,self.destinataire,self.obj,self.msg)
        if is_okay:
            self.show_dialog("Lettre créée avec succès")
        else:
            self.show_dialog("Erreur lors de la création de la lettre",True)
           
    def create_json(self):
        self.associate()
        exp_json = {'expediteur':{'nom':self.expediteur.nom,
                    'prenom':self.expediteur.prenom,
                    'adresse':self.expediteur.adresse,
                    'cp':self.expediteur.cp,
                    'ville':self.expediteur.ville,
                    'tel':self.expediteur.tel,
                    'mail':self.expediteur.mail
                    }}
        try:
            f= open("data/settings.json","w")
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
    
    def on_stop(self):
        self.manager.create_json()
    
LetterGenerator().run()

import json
import os.path
from tkinter import BooleanVar
from object.Person import Person
from object.Lettre import Letter

class JSON_manager():
    
    def __init__(self,root) :
        self.root = root
    
    def create_json(self):
        self.root.associate()
        if self.root.s_active.get():
            exp_json = {'nom': self.root.expediteur.nom,
                        'prenom': self.root.expediteur.prenom,
                        'adresse': self.root.expediteur.adresse,
                        'cp': self.root.expediteur.cp,
                        'ville': self.root.expediteur.ville,
                        'tel': self.root.expediteur.tel,
                        'mail': self.root.expediteur.mail
                                    }
        settings_json = {'Lock': self.root.e_active.get(),
                        'Save': self.root.s_active.get()}
        
        try:
            if self.root.s_active.get():
                f = open("data/data.json", "w")
                json.dump(exp_json, f)
                f.close()
            f = open("data/settings.json", "w")
            json.dump(settings_json, f)
            f.close()
            print("Les JSON a été créé")
        except:
            print("Erreur lors de la création du fichier JSON")
    
    def load_json(self):
        self.root.destinataire = Person()
        self.root.letter = Letter(self.root)
        self.root.e_active = BooleanVar()
        self.root.s_active = BooleanVar()
        if os.path.isfile("data/settings.json"):
            f = open('data/settings.json', 'r')
            data_json = f.read()
            data = json.loads(data_json)
            f.close()
            self.root.e_active.set(data['Lock'])
            self.root.s_active.set(data['Save'])
        else:
            self.root.e_active.set(False)
            self.root.s_active.set(True)
            
        if os.path.isfile("data/data.json") and self.root.s_active.get():
            f = open('data/data.json', 'r')
            data_json = f.read()
            data = json.loads(data_json)
            f.close()
            self.root.expediteur = Person(data['nom'],
                                     data['prenom'],
                                     data['adresse'],
                                     data['cp'],
                                     data['ville'],
                                     data['tel'],
                                     data['mail'])
            print("JSON loaded")
        else:
            print("JSON not found")
            self.root.expediteur = Person()
        
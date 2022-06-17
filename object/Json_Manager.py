import json
import os.path
from object.Person import Person
from object.Lettre import Letter

class JSON_manager():
    
    def __init__(self,root) :
        self.root = root
    
    def create_json(self):
        self.root.associate()
        exp_json = {'expediteur': {'nom': self.root.expediteur.nom,
                    'prenom': self.root.expediteur.prenom,
                                   'adresse': self.root.expediteur.adresse,
                                   'cp': self.root.expediteur.cp,
                                   'ville': self.root.expediteur.ville,
                                   'tel': self.root.expediteur.tel,
                                   'mail': self.root.expediteur.mail
                                   }}
        try:
            f = open("data/settings.json", "w")
            json.dump(exp_json, f)
            print("Le JSON a été créé")
            f.close()
        except:
            print("Erreur lors de la création du fichier JSON")
    
    def load_json(self):
        self.root.destinataire = Person()
        self.root.letter = Letter(self.root)
        if os.path.isfile("data/settings.json"):
            f = open('data/settings.json', 'r')
            data_json = f.read()
            data = json.loads(data_json)
            data_e = data.get('expediteur')
            f.close()
            self.root.expediteur = Person(data_e['nom'],
                                     data_e['prenom'],
                                     data_e['adresse'],
                                     data_e['cp'],
                                     data_e['ville'],
                                     data_e['tel'],
                                     data_e['mail'])
            print("JSON loaded")
        else:
            print("JSON not found")
            self.root.expediteur = Person()
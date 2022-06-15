from kivy.properties import NumericProperty, Clock, ObjectProperty, StringProperty

class Person:
    
    def __init__(self,nom="",prenom="",adresse="",cp="",ville="",tel = "", mail = ""):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.cp = cp
        self.ville = ville
        self.tel = tel
        self.mail = mail
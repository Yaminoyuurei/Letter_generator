class Person:
    
    def __init__(self,nom,prenom,adresse,cp,ville,tel = "", mail = ""):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.cp = cp
        self.ville = ville
        self.tel = tel
        self.mail = mail
    
    def check(self):
        text = f"{self.nom} {self.prenom}\n{self.adresse}\n{self.cp} {self.ville}"
        if self.tel == "" and self.mail == "":
            return text
        elif self.tel != "" and self.mail == "":
            return text+f"\nTel : {self.tel}"
        elif self.tel == "" and self.mail != "":
            return text+f"\nMail : {self.mail}"
        else:
            return text+f"\nTel : {self.tel}\nMail : {self.mail}"
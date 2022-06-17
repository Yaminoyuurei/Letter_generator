from tkinter import *
from tkinter import ttk, messagebox
def create(self):
        tabsystem = ttk.Notebook(self, width=300)

        # Create new tabs using Frame widget
        tab1 = Frame(tabsystem)
        tab2 = Frame(tabsystem)
        tab3 = Frame(tabsystem)

        tabsystem.add(tab1, text='Expéditeur')
        tabsystem.add(tab2, text='Destinataires')
        tabsystem.add(tab3, text='Références')
        tabsystem.pack(side=LEFT, fill=Y)

        frame_tab1 = Frame(tab1)
        self.e_nom = self.create_label(frame_tab1, "Nom :",self.expediteur.nom)
        self.e_prenom = self.create_label(frame_tab1, "Prénom :",self.expediteur.prenom)
        self.e_adresse = self.create_label(frame_tab1, "Adresse :",self.expediteur.adresse, 3)
        self.e_cp = self.create_label(frame_tab1, "Code postal :",self.expediteur.cp)
        self.e_ville = self.create_label(frame_tab1, "Ville :",self.expediteur.ville)
        self.e_tel = self.create_label(frame_tab1, "Téléphone :",self.expediteur.tel)
        self.e_mail = self.create_label(frame_tab1, "Email :",self.expediteur.mail)
        self.e_active = BooleanVar()
        self.is_active = Checkbutton(frame_tab1, text="Verrouiller", variable=self.e_active,
                                     onvalue=True, offvalue=False, command=self.disable_all)
        self.is_active.pack(pady=5, anchor=W)
        frame_tab1.pack(fill=Y)

        frame_tab2 = Frame(tab2)
        self.d_nom = self.create_label(frame_tab2, "Nom :",self.destinataire.nom)
        self.d_prenom = self.create_label(frame_tab2, "Prénom :",self.destinataire.prenom)
        self.d_adresse = self.create_label(frame_tab2, "Adresse :", self.destinataire.adresse ,3)
        self.d_cp = self.create_label(frame_tab2, "Code postal :",self.destinataire.cp)
        self.d_ville = self.create_label(frame_tab2, "Ville :",self.destinataire.ville)
        frame_tab2.pack(fill=Y)
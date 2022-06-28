from tkinter import *
from tkinter import ttk
def create(self):
        s=ttk.Style()
        
        tabsystem = ttk.Notebook(self, width=300)
        s.configure('.', font=('Arial', 12))

        # Create new tabs using Frame widget
        tab1 = Frame(tabsystem, bg=self.bg_color)
        tab2 = Frame(tabsystem, bg=self.bg_color)
        tab3 = Frame(tabsystem, bg=self.bg_color)

        tabsystem.add(tab1, text='Expéditeur')
        tabsystem.add(tab2, text='Destinataires')
        tabsystem.add(tab3, text='Références')
        tabsystem.pack(side=LEFT, fill=Y)

        frame_tab1 = Frame(tab1, bg=self.bg_color)
        self.e_nom = self.create_label(frame_tab1, "Nom :",self.expediteur.nom)
        self.e_prenom = self.create_label(frame_tab1, "Prénom :",self.expediteur.prenom)
        self.e_adresse = self.create_label(frame_tab1, "Adresse :",self.expediteur.adresse, 3)
        self.e_cp = self.create_label(frame_tab1, "Code postal :",self.expediteur.cp)
        self.e_ville = self.create_label(frame_tab1, "Ville :",self.expediteur.ville)
        self.e_tel = self.create_label(frame_tab1, "Téléphone :",self.expediteur.tel)
        self.e_mail = self.create_label(frame_tab1, "Email :",self.expediteur.mail)
        frame_tab1.pack(fill=BOTH)

        frame_tab2 = Frame(tab2, bg=self.bg_color)
        self.d_nom = self.create_label(frame_tab2, "Nom :")
        self.d_prenom = self.create_label(frame_tab2, "Prénom :")
        self.d_adresse = self.create_label(frame_tab2, "Adresse :",ligne = 3)
        self.d_cp = self.create_label(frame_tab2, "Code postal :")
        self.d_ville = self.create_label(frame_tab2, "Ville :")
        frame_tab2.pack(fill=BOTH)
        
        frame_tab3 = Frame(tab3, bg=self.bg_color)
        self.ar = BooleanVar()
        self.r_ar = Checkbutton(frame_tab3, font=("Arial", 12), text="Lettre recommandée avec A.R", variable=self.ar)
        self.r_ar.config(bg=self.bg_color, fg=self.fg_color, activebackground=self.bg_color, activeforeground=self.fg_color, selectcolor=self.bg_color)
        self.r_ar.pack(padx=5, pady=5, anchor=W)
        self.r_vref = self.create_label(frame_tab3, "Vérification de référence :")
        self.r_nref = self.create_label(frame_tab3, "Numéro de référence :")
        self.r_pj = self.create_label(frame_tab3, "Pièce jointe :")
        self.r_attention = self.create_label(frame_tab3, "Attention :")
        frame_tab3.pack(fill=BOTH)
        
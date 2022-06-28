from tkinter import *

def create(self):
        menu_bar = Menu(self,font=("Arial", 12), bg=self.bg_color, fg=self.fg_color)

        menu_file = Menu(menu_bar, tearoff=0,font=("Arial", 12), bg=self.bg_color, fg=self.fg_color)
        menu_file.add_command(label="Nouveau", command=self.do_something, state=DISABLED)
        menu_file.add_separator()
        menu_file.add_command(label="Enregistrer sous...", command=self.create_letter)

        menu_import = Menu(menu_file, tearoff=0,font=("Arial", 12), bg=self.bg_color, fg=self.fg_color)
        menu_import.add_command(label="Base Excel", command=self.do_something)
        menu_file.add_cascade(label="Importer", menu=menu_import, state=DISABLED)

        menu_file.add_separator()
        menu_file.add_command(label="Quitter", command=self.quit)
        menu_bar.add_cascade(label="Fichier", menu=menu_file)

        menu_outils = Menu(menu_bar, tearoff=0,font=("Arial", 12), bg=self.bg_color, fg=self.fg_color)
        menu_outils.add_checkbutton(label="Verrouiller l'expéditeur", variable=self.e_active,
                                     onvalue=True, offvalue=False, command=self.disable_all, activeforeground=self.fg_color, selectcolor=self.fg_color)
        menu_outils.add_checkbutton(label="Sauvegarde automatique de l'expéditeur", variable=self.s_active,
                                     onvalue=True, offvalue=False, command=self.disable_all, activeforeground=self.fg_color, selectcolor=self.fg_color)
        menu_bar.add_cascade(label="Préférences", menu=menu_outils)

        menu_help = Menu(menu_bar, tearoff=0,font=("Arial", 12), bg=self.bg_color, fg=self.fg_color)
        menu_help.add_command(label="À propos...", command=self.do_about)
        menu_bar.add_cascade(label="Aide", menu=menu_help)

        self.config(menu=menu_bar)
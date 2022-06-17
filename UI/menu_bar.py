from tkinter import *


def create(self):
        menu_bar = Menu(self)

        menu_file = Menu(menu_bar, tearoff=0)
        menu_file.add_command(label="Nouveau", command=self.do_something)
        menu_file.add_command(label="Ouvrir", command=self.do_something)
        menu_file.add_separator()
        menu_file.add_command(label="Enregistrer sous...", command=self.create_letter)

        menu_import = Menu(menu_file, tearoff=0)
        menu_import.add_command(label="Base Excel", command=self.do_something)
        menu_file.add_cascade(label="Importer", menu=menu_import)

        menu_file.add_separator()
        menu_file.add_command(label="Quitter", command=self.quit)
        menu_bar.add_cascade(label="Fichier", menu=menu_file)

        menu_edit = Menu(menu_bar, tearoff=0)
        menu_edit.add_command(label="Annuler", command=self.do_something)
        menu_edit.add_separator()
        menu_edit.add_command(label="Copier", command=self.do_something)
        menu_edit.add_command(label="Couper", command=self.do_something)
        menu_edit.add_command(label="Coller", command=self.do_something)
        menu_bar.add_cascade(label="Editer", menu=menu_edit)

        menu_outils = Menu(menu_bar, tearoff=0)
        menu_outils.add_command(label="Préférences", command=self.do_something)
        menu_bar.add_cascade(label="Outils", menu=menu_outils)

        menu_help = Menu(menu_bar, tearoff=0)
        menu_help.add_command(label="À propos...", command=self.do_about)
        menu_bar.add_cascade(label="Aide", menu=menu_help)

        self.config(menu=menu_bar)
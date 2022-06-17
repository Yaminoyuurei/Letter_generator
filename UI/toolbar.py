from tkinter import *
from UI.menu_bar import create


def create(self):

        toolbar = Frame(self)
        newButton = Button(toolbar, text="Nouveau", command=self.do_something)
        newButton.pack(side=LEFT, padx=2, pady=2)
        saveButton = Button(toolbar, text="Générer",
                            command=self.create_letter)
        saveButton.pack(side=LEFT, padx=2, pady=2)
        settingsButton = Button(toolbar, text="Settings",
                                command=self.do_something)
        settingsButton.pack(side=RIGHT, padx=2, pady=2)

        toolbar.pack(side=TOP, fill=X)
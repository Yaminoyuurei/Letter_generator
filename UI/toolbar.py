from tkinter import *
from UI.menu_bar import create

def create(self):

        toolbar = Frame(self, bg=self.bg_color)
        newButton = Button(toolbar, text="Nouveau",font=("Arial",12), command=self.do_something, fg=self.fg_color, bg=self.bg_color_text)
        newButton.pack(side=LEFT, padx=2, pady=2)
        saveButton = Button(toolbar, text="Générer",font=("Arial",12),
                            command=self.create_letter, fg=self.fg_color, bg=self.bg_color_text)
        saveButton.pack(side=LEFT, padx=2, pady=2)

        toolbar.pack(side=TOP, fill=X)
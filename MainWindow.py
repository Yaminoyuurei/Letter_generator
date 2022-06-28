from email.base64mime import header_length
from ntpath import join
from tkinter import *
from tkinter import ttk, messagebox
from tkinter import filedialog
from turtle import color
from object.Lettre import Letter
import UI.tab as tab
import UI.menu_bar as menu_bar
import UI.toolbar as toolbar
from object.Json_Manager import JSON_manager


class MainWindow(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.bg_color_text = "#1e1e1e"
        self.bg_color = "#333333"
        self.fg_color = "#ffffff"
        self.json_manager = JSON_manager(self)
        self.json_manager.load_json()
        menu_bar.create(self)
        toolbar.create(self)
        tab.create(self)
        self.create_body()
        self.disable_all()

    def create_body(self):
        body = Frame(self, bg=self.bg_color)
        self.m_obj = self.create_label(body, "Objet :")
        self.m_core = self.create_label(body, "Corps :", extend=True)
        body.pack(fill=BOTH, expand=True)

    def create_label(self, frame, label, Object="", ligne=1, extend=False):
        if extend:
            label = Label(frame, font=("Arial", 12), text=label)
            label.config(fg=self.fg_color, bg=self.bg_color)
            text = Text(frame, font=("Arial", 12),
                        insertbackground=self.fg_color, state=NORMAL, spacing3=10)
            text.config(fg=self.fg_color, bg=self.bg_color_text)
            label.pack(padx=5, pady=5, anchor=W)
            text.pack(padx=5, pady=5, fill=BOTH, expand=True)
            text.insert('1.0', Object)
        elif ligne > 1:
            label = Label(frame, font=("Arial", 12), text=label, wrap=None)
            label.config(fg=self.fg_color, bg=self.bg_color)
            text = Text(frame, font=("Arial", 12),insertbackground=self.fg_color, height=ligne, state=NORMAL)
            text.config(fg=self.fg_color, bg=self.bg_color_text)
            label.pack(padx=5, pady=5, anchor=W)
            text.pack(padx=5, pady=5, fill=X)
            text.insert('1.0', Object)
        else:
            label = Label(frame, font=("Arial", 12), text=label)
            label.config(fg=self.fg_color, bg=self.bg_color)
            text = Entry(frame, font=("Arial", 12),insertbackground=self.fg_color, state=NORMAL)
            text.config(fg=self.fg_color, bg=self.bg_color_text)
            label.pack(padx=5, pady=5, anchor=W)
            text.pack(padx=5, pady=5, fill=X)
            text.insert("1", Object)
        return(label, text)

    def disable_all(self):
        if self.e_active.get():
            self.e_nom[1].config(state=DISABLED)
            self.e_prenom[1].config(state=DISABLED)
            self.e_adresse[1].config(state=DISABLED)
            self.e_cp[1].config(state=DISABLED)
            self.e_ville[1].config(state=DISABLED)
            self.e_tel[1].config(state=DISABLED)
            self.e_mail[1].config(state=DISABLED)
        else:
            self.e_nom[1].config(state=NORMAL)
            self.e_prenom[1].config(state=NORMAL)
            self.e_adresse[1].config(state=NORMAL)
            self.e_cp[1].config(state=NORMAL)
            self.e_ville[1].config(state=NORMAL)
            self.e_tel[1].config(state=NORMAL)
            self.e_mail[1].config(state=NORMAL)

    def do_something(self):
        messagebox.showerror(
            "ERREUR", "La fonctionnalité n'est pas encore implémentée")

    def show_dialog(self, title, message, type="info"):
        if type == "info":
            messagebox.showinfo(title, message)
        elif type == "error":
            messagebox.showerror(title, message)
        elif type == "warning":
            messagebox.showwarning(title, message)
        elif type == "question":
            q = messagebox.askokcancel(title, message)
            return q

    def do_about(self):
        messagebox.showinfo("My title", "My message")

    def associate(self):
        # Mise à jour de l'expéditeur
        self.expediteur.nom = self.get_text(self.e_nom).upper()
        self.expediteur.prenom = self.get_text(self.e_prenom).capitalize()
        self.expediteur.adresse = self.get_text(self.e_adresse)
        self.expediteur.cp = self.get_text(self.e_cp)
        self.expediteur.ville = self.get_text(self.e_ville).upper()
        self.expediteur.tel = self.get_text(self.e_tel)
        self.expediteur.mail = self.get_text(self.e_mail)
        # # Mise à jour du destinataire
        self.destinataire.nom = self.get_text(self.d_nom).upper()
        self.destinataire.prenom = self.get_text(self.d_prenom).capitalize()
        self.destinataire.adresse = self.get_text(self.d_adresse)
        self.destinataire.cp = self.get_text(self.d_cp)
        self.destinataire.ville = self.get_text(self.d_ville).upper()
        # Mise à jour du Message
        self.obj = self.get_text(self.m_obj)
        self.msg = self.get_text(self.m_core)

    def get_text(self, text):
        try:
            data = text[1].get(1.0, END).split("\n")
            data.pop(-1)
            data_j = "\n".join(data)
            return data_j
        except:
            return text[1].get()

    def create_letter(self):
        self.associate()
        is_okay = self.letter.save_letter(
            self.expediteur, self.destinataire, self.obj, self.msg)
        if not is_okay:
            self.show_dialog(
                "Génération", "Une erreur est survenue lors de la sauvegarde de la lettre", type="error")

    def test(self):
        text = self.get_text(self.m_core)
        messagebox.showinfo("TEST", text)
        print(text)

    def file_manager(self, type, name, extension,):
        if type == "open":
            f = filedialog.askopenfilename()
        elif type == "save":
            f = filedialog.asksaveasfilename(
                initialfile=name, defaultextension=extension, filetypes=[(extension, f".{extension}")])
        return f

    def quit(self):
        self.json_manager.create_json()
        self.destroy()

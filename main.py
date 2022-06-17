from tkinter import *

from MainWindow import MainWindow


window = MainWindow()
window.title("Letter Generator")
window.iconbitmap("assets/icon.ico")
window.minsize(600, 600)
window.protocol("WM_DELETE_WINDOW", window.quit)
window.mainloop()

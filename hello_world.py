# coding : utf-8  

from tkinter import *

fenetre = Tk()

label = Label(fenetre, text="Hello World")
label.pack()

# bouton de sortie
button = Button(fenetre, text="Fermer", command=fenetre.quit)
button.pack()

fenetre.mainloop()
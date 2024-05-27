# coding : utf-8 
# code de base du gui

from tkinter import *
from tkinter.messagebox import *

fenetre_main = Tk()

def alert():
    showinfo("alerte", "Bravo !")

menubar = Menu(fenetre_main)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Créer", command=alert)
menu1.add_command(label="Editer", command=alert)
menu1.add_separator()

menu1.add_command(label = "Quitter", command=fenetre_main.quit)
menubar.add_cascade(label="Fichier", menu=menu1)


menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Couper", command=alert)
menu2.add_command(label="Copier", command=alert)
menu2.add_command(label="Coller", command=alert)
menubar.add_cascade(label="Editer", menu=menu2)

fenetre_main.config(menu=menubar)


def recupere():
    showinfo("Alerte", entree.get())

value = StringVar()
value.set("Valeur")
entree = Entry(fenetre_main, textvariable=value, width=30)
entree.pack()

bouton = Button(fenetre_main, text="Valider", command=recupere)
bouton.pack()





fenetre_main.mainloop()
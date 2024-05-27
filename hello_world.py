# coding : utf-8  
# bon c'est un fichier avec full fonctions de test pour tkinter

from tkinter import *

fenetre = Tk()
fenetre['bg']='white'

label = Label(fenetre, text="Hello World")
label.pack()

# bouton de sortie
button = Button(fenetre, text="Fermer", command=fenetre.quit)
button.pack()

# test du radiobutton
value = StringVar()
bouton1 = Radiobutton(fenetre, text="Oui",variable=value, value=1)
bouton2 = Radiobutton(fenetre, text="Non",variable=value, value=2)
bouton3 = Radiobutton(fenetre, text="Peut-être en fait",variable=value, value=3)

bouton1.pack()
bouton2.pack()
bouton3.pack()

# test des listes

liste = Listbox(fenetre)
liste.insert(1, "Python")
liste.insert(2, "PHP")
liste.insert(3, "ROS")
liste.insert(4, "Arduino")

liste.pack()


# test du canva :

canvas = Canvas(fenetre, width=150, height=120, background='white')
txt = canvas.create_text(75,60, text="OUI AHH NOON AAAH", font="Arial 16 italic", fill="green")
canvas.pack()

# test des frames :

# frame 1
Frame1 = Frame(fenetre,borderwidth=1, relief=GROOVE)
BoutonFrame = Button(Frame1, text="fermer aussi", command=fenetre.quit)

BoutonFrame.pack(side=LEFT, padx=5, pady=5)
Frame1.pack(side=LEFT, padx = 30, pady=50)

Label(Frame1, text="Frame 1").pack(padx=10, pady=10)

fenetre.mainloop()
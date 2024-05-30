# coding : utf-8 
# code de base du gui

from tkinter import *
from tkinter.messagebox import *

fenetre_main = Tk()
# définitions des variables position x,y , vitesse linéaire , vitesse angulaire ...
x = 0
y =0
Rz=0 
Vx=0
Vy=0
Vrz=0
def alert():
    showinfo("alerte", "Bravo !")

# bar des menus

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



# définition des différentes frames et du layout:

Frame1 = Frame(fenetre_main,borderwidth=2, relief=GROOVE,width=200, height=300).place(x=10,y=10)
Frame2 = Frame(fenetre_main,borderwidth=2, relief=GROOVE,width=200, height=300).place(x=210,y=10)
Frame3 = Frame(fenetre_main,borderwidth=2, relief=GROOVE,width=400, height=300).place(x=410,y=10)
Frame4 = Frame(fenetre_main,borderwidth=2, relief=GROOVE,width=200, height=200).place(x=10,y=310)
Frame5 = Frame(fenetre_main,borderwidth=2, relief=GROOVE,width=600, height=200).place(x=210,y=310)

Label(Frame1, text="Infos Robot").place(x=60,y=20)
Label(Frame2, text="Etat de la connexion").place(x=250,y=20)
Label(Frame3, text="Visualisation").place(x=550,y=20)
Label(Frame4, text="Commande").place(x=60,y=320)
Label(Frame5, text="graphiques").place(x=500,y=320)

# PARTIE COMMANDE :

BoutonAvancer = Button(Frame4, text="⬆", borderwidth=1, relief=RAISED).place(in_=Frame4,x=60,y=400)
BoutonReculer = Button(Frame4, text="⬇", borderwidth=1, relief=RAISED).place(in_=Frame4,x=60,y=450)
BoutonRotationDroite = Button(Frame4, text="⟳", borderwidth=1, relief=RAISED).place(in_=Frame4,x=85,y=425)
BoutonRotationGauche = Button(Frame4, text="⟲", borderwidth=1, relief=RAISED).place(in_=Frame4,x=30,y=425)

BoutonStartStop = Button(Frame4, text="Start/Stop", borderwidth=1, relief=RAISED).place(in_=Frame4,x=40,y=350)
BoutonAvancer.pack()
BoutonReculer.pack()
BoutonRotationDroite.pack()
BoutonRotationGauche.pack()
BoutonStartStop.pack()
# curseurs :

valueSpeed = DoubleVar()
valueAcceleration = DoubleVar()

scaleSpeed = Scale(fenetre_main, variable=valueSpeed)
scaleAcceleration = Scale(fenetre_main, variable=valueAcceleration)
scaleSpeed.place(in_=Frame4, x=105, y=375)
scaleAcceleration.place(in_=Frame4, x=145, y=375)

Label(Frame4, text="Speed").place(in_=Frame4,x=115,y=355)
Label(Frame4, text="Acc").place(in_=Frame4,x=165,y=355)

# définition des fonctions activées une fois les boutons pressés  

def bouton_haut():
	global BoutonAvancer
	BoutonAvancer.config(y=y+0.01)
def bouton_bas():
	global BoutonReculer
	BoutonAvancer.config(y=y-0.01)
def bouton_rotdroit():
	global BoutonRotationDroite
	BoutonRotationDroite.config(Rz=Rz+0.1)
def bouton_rotgauche():
	global BoutonRotationDroite
	BoutonRotationDroite.config(Rz=Rz+0.1)
def bouton_stop():
	global BoutonStartStop
	BoutonStartStop.config(Rz=0,x=0,y=0)

# on configure les boutons avec la fonction attribués lorsqu'on appui dessus 

BoutonAvancer.config(command = bouton_haut)
BoutonReculer.config(command = bouton_bas)
BoutonRotationDroite.config(command = bouton_rotdroit)
BoutonRotationGauche.config(command = bouton_rotgauche)
BoutonStartStop.config(command = bouton_stop)
# value = StringVar()
# value.set("Valeur")
# entree = Entry(Frame1, textvariable=value, width=30)
# entree.grid(row=1,column=1)

# bouton = Button(Frame1, text="Valider", command=recupere)
# bouton.grid(row=1,column=1)



fenetre_main.mainloop()

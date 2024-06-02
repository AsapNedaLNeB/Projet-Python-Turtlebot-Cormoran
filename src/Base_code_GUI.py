# coding : utf-8 
# Code de base du GUI

from tkinter import *
from tkinter.messagebox import *

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Application GUI")

        # Barre de menu
        self.menubar = Menu(master)

        self.menu1 = Menu(self.menubar, tearoff=0)
        self.menu1.add_command(label="Créer", command=self.alert)
        self.menu1.add_command(label="Editer", command=self.alert)
        self.menu1.add_separator()
        self.menu1.add_command(label="Quitter", command=master.quit)
        self.menubar.add_cascade(label="Fichier", menu=self.menu1)

        self.menu2 = Menu(self.menubar, tearoff=0)
        self.menu2.add_command(label="Couper", command=self.alert)
        self.menu2.add_command(label="Copier", command=self.alert)
        self.menu2.add_command(label="Coller", command=self.alert)
        self.menubar.add_cascade(label="Editer", menu=self.menu2)

        master.config(menu=self.menubar)

        # Définition des différents cadres (ou frames)
        self.create_frames()

    def alert(self):
        showinfo("alerte", "Bravo !")

    def create_frames(self):
        # Frame1: Infos Robot
        self.frame1 = Frame(self.master, borderwidth=2, relief=GROOVE, width=200, height=300)
        self.frame1.place(x=10, y=10)
        Label(self.frame1, text="Infos Robot").place(x=60, y=20)

        # Frame2: Etat de la connexion
        self.frame2 = Frame(self.master, borderwidth=2, relief=GROOVE, width=200, height=300)
        self.frame2.place(x=210, y=10)
        Label(self.frame2, text="Etat de la connexion").place(x=60, y=20)

        # Frame3: Visualisation
        self.frame3 = Frame(self.master, borderwidth=2, relief=GROOVE, width=400, height=300)
        self.frame3.place(x=410, y=10)
        Label(self.frame3, text="Visualisation").place(x=60, y=20)

        # Frame4: Commande
        self.frame4 = Frame(self.master, borderwidth=2, relief=GROOVE, width=200, height=200)
        self.frame4.place(x=10, y=310)
        Label(self.frame4, text="Commande").place(x=60, y=20)

        # Frame5: Graphiques
        self.frame5 = Frame(self.master, borderwidth=2, relief=GROOVE, width=600, height=200)
        self.frame5.place(x=210, y=310)
        Label(self.frame5, text="graphiques").place(x=500, y=20)

        # Boutons de commande
        self.create_command_buttons()

        # Curseurs
        self.create_sliders()

    def create_command_buttons(self):
        Button(self.frame4, text="⬆", borderwidth=1, relief=RAISED).place(x=60, y=400)
        Button(self.frame4, text="⬇", borderwidth=1, relief=RAISED).place(x=60, y=450)
        Button(self.frame4, text="⟳", borderwidth=1, relief=RAISED).place(x=85, y=425)
        Button(self.frame4, text="⟲", borderwidth=1, relief=RAISED).place(x=30, y=425)
        Button(self.frame4, text="Start/Stop", borderwidth=1, relief=RAISED).place(x=40, y=350)

    def create_sliders(self):
        Label(self.frame4, text="Speed").place(x=115, y=355)
        Label(self.frame4, text="Acc").place(x=165, y=355)
        Scale(self.frame4, from_=0, to=100).place(x=105, y=375)
        Scale(self.frame4, from_=0, to=100).place(x=145, y=375)

        # Entrée de texte
        self.create_text_entry()

    def create_text_entry(self):
        Label(self.frame1, text="Valeur").place(x=60, y=50)
        self.entry = Entry(self.frame1, width=30)
        self.entry.place(x=10, y=80)
        Button(self.frame1, text="Valider", command=self.show_entry_value).place(x=80, y=120)

    def show_entry_value(self):
        value = self.entry.get()
        showinfo("Alerte", value)


def main():
    fenetre_main = Tk()
    app = GUI(fenetre_main)
    fenetre_main.mainloop()

if __name__ == "__main__":
    main()
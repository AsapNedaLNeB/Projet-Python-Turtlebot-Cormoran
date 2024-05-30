import tkinter as tk

class CommandFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.avance_button = tk.Button(self, text="avance", command=self.move_avance)
        self.avance_button.pack(fill=tk.X)
        
        self.recule_button = tk.Button(self, text="recule", command=self.move_recule)
        self.recule_button.pack(fill=tk.X)
        
        self.gauche_button = tk.Button(self, text="gauche", command=self.move_gauche)
        self.gauche_button.pack(fill=tk.X)
        
        self.droite_button = tk.Button(self, text="droite", command=self.move_droite)
        self.droite_button.pack(fill=tk.X)
        
        self.vitesse_label = tk.Label(self, text="Vitesse Linéaire:")
        self.vitesse_label.pack()
        
        self.vitesse_slider = tk.Scale(self, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL)
        self.vitesse_slider.pack(fill=tk.X)
        
        self.vitesse_ang_label = tk.Label(self, text="Vitesse Angulaire:")
        self.vitesse_ang_label.pack()
        
        self.vitesse_ang_slider = tk.Scale(self, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL)
        self.vitesse_ang_slider.pack(fill=tk.X)
        
    def move_avance(self):
        # Logic to move the robot avance
        print("avance")
        
    def move_recule(self):
        # Logic to move the robot recule
        print("recule")
        
    def move_gauche(self):
        # Logic to turn the robot gauche
        print("gauche")
        
    def move_droite(self):
        # Logic to turn the robot droite
        print("droite")
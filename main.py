import tkinter as tk
from movement_frame import MovementFrame
from command_frame import CommandFrame
from robot_controller import TurtleBot3Controller
from Gazebo_launch import launch_gazebo

class RobotApp(tk.Tk):
    def __init__(self):
        # Initialisation de la fenêtre principale
        super().__init__()
        self.title("TurtleBot Controller")
        
        # Initialisation du contrôleur de robot
        self.robot_controller = TurtleBot3Controller()
        
        # Ajoute et configure le cadre de mouvement
        self.movement_frame = MovementFrame(self, self.robot_controller)
        self.movement_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Ajoute et configure le cadre de commande
        self.command_frame = CommandFrame(self, self.robot_controller)
        self.command_frame.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Lie les touches de direction aux mouvements du robot
        self.bind_keys()

    def bind_keys(self):
        # Associe les touches du clavier aux commandes de mouvement du robot
        self.bind('<z>', lambda event: self.robot_controller.move(0.2, 0.0, 1))  # Avancer
        self.bind('<s>', lambda event: self.robot_controller.move(-0.2, 0.0, 1)) # Reculer
        self.bind('<q>', lambda event: self.robot_controller.move(0.0, 0.5, 1))  # Tourner à gauche
        self.bind('<d>', lambda event: self.robot_controller.move(0.0, -0.5, 1)) # Tourner à droite
        self.bind('<KeyRelease>', self.stop_robot)                               # Arrêter le robot

    def stop_robot(self, event):
        # Arrête le robot
        self.robot_controller.move(0.0, 0.0, 1.0)

if __name__ == "__main__":
    # Lance Gazebo avant de démarrer l'application
    launch_gazebo()
    # Crée et lance l'application Tkinter
    app = RobotApp()
    app.mainloop()
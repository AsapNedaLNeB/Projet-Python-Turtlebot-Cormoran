import tkinter as tk
from movement_frame import MovementFrame
from command_frame import CommandFrame
from robot_controller import TurtleBot3Controller
from Gazebo_launch import launch_gazebo

class RobotApp(tk.Tk):
    def __init__(self):
        super().__init__() #initialisation des différents scripts
        self.title("TurtleBot Controller")
        
        self.robot_controller = TurtleBot3Controller()
        
        self.movement_frame = MovementFrame(self, self.robot_controller)
        self.movement_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.command_frame = CommandFrame(self, self.robot_controller)
        self.command_frame.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.bind_keys()

    def bind_keys(self): #move(vitesse,vitesse angulaire,durée)
        self.bind('<z>', lambda event: self.robot_controller.move(0.2, 0.0, 1))
        self.bind('<s>', lambda event: self.robot_controller.move(-0.2, 0.0, 1))
        self.bind('<q>', lambda event: self.robot_controller.move(0.0, 0.5, 1))
        self.bind('<d>', lambda event: self.robot_controller.move(0.0, -0.5, 1))
        self.bind('<KeyRelease>', self.stop_robot)

    def stop_robot(self, event):
        self.robot_controller.move(0.0, 0.0, 1.0)

if __name__ == "__main__":
    launch_gazebo()
    app = RobotApp()
    app.mainloop()
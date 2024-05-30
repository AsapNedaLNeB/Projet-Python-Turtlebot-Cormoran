import tkinter as tk
from connection_frame import ConnectionFrame
from movement_frame import MovementFrame
from command_frame import CommandFrame
from robot_controler import RobotController

class RobotApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TurtleBot Controller")
        
        self.robot_controller = RobotController()
        
        self.connection_frame = ConnectionFrame(self, self.robot_controller)
        self.connection_frame.pack(side=tk.TOP, fill=tk.X)

        self.movement_frame = MovementFrame(self, self.robot_controller)
        self.movement_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.command_frame = CommandFrame(self, self.robot_controller)
        self.command_frame.pack(side=tk.RIGHT, fill=tk.Y)

if __name__ == "__main__":
    app = RobotApp()
    app.mainloop()
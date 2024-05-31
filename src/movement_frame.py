import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class MovementFrame(tk.Frame):
    def __init__(self, parent, robot_controller):
        super().__init__(parent)
        self.robot_controller = robot_controller
        
        self.fig, self.ax = plt.subplots(2, 1)
        
        self.line_position, = self.ax[0].plot([], [], 'r-')
        self.line_velocity, = self.ax[1].plot([], [], 'b-')
        
        self.ax[0].set_title("Robot Position (x, y)")
        self.ax[1].set_title("Robot Velocity (linear, angular)")
        
        self.ax[0].set_xlim(0, 10)
        self.ax[0].set_ylim(0, 10)
        self.ax[1].set_xlim(0, 10)
        self.ax[1].set_ylim(-1, 1)
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        self.ani = animation.FuncAnimation(self.fig, self.update_graph, interval=500)
        
    def update_graph(self, i):
        if self.robot_controller.current_pose:
            x = self.robot_controller.current_pose.position.x
            y = self.robot_controller.current_pose.position.y
            self.line_position.set_data([0, x], [0, y])
            # Add logic for velocity if available
        self.canvas.draw()

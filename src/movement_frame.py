import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

data=[[(0,0),(0,0)]]

class MovementFrame(tk.Frame):
    def __init__(self, parent, robot_controller):
        super().__init__(parent)
        self.robot_controller = robot_controller
        
        self.fig, self.ax = plt.subplots(2, 1)
        
        self.line_position, = self.ax[0].plot([], [], 'r-')
        self.line_velocity, = self.ax[1].plot([], [], 'b-')
        
        self.ax[0].set_title("Position (x, y)")
        self.ax[1].set_title("Vitesse en m.s⁻1 et rad.s⁻1")
        
        self.ax[0].set_xlim(-10, 10)
        self.ax[0].set_ylim(-10, 10)
        self.ax[1].set_xlim(0, 1)
        self.ax[1].set_ylim(-10, 0.02)
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        self.ani = animation.FuncAnimation(self.fig, self.update_graph, interval=500)
        
    def update_graph(self,i) -> None: #grosses optimisations possibles mais pas prioritaires
        if self.robot_controller.current_pose:
            x = self.robot_controller.current_pose.position.x
            y = self.robot_controller.current_pose.position.y
            data.append([(x,y),((x-data[len(data)-1][0][0])/1,(y-data[len(data)-1][0][1])/1)])
            speed = [np.sqrt(a[1][0]**2+a[1][1]**2) for a in data]
            yscale=max(max(speed),0.02)
            self.ax[1].set_xlim(0, len(data))
            self.ax[1].set_ylim(-0.005, yscale)
            self.line_position.set_data([a[0][0] for a in data], [a[0][1] for a in data])
            self.line_velocity.set_data([t for t in range(len(data))],speed)
        self.canvas.draw()

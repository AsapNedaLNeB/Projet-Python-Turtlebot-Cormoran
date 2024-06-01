#gère le controle du turtlebot

import tkinter as tk

class CommandFrame(tk.Frame):
    def __init__(self, parent, robot_controller): #met en place les différents boutons et sliders de commande
        super().__init__(parent)
        self.robot_controller = robot_controller
        
        self.forward_button = tk.Button(self, text="Avance", command=self.move_forward)
        self.forward_button.pack(fill=tk.X)
        
        self.backward_button = tk.Button(self, text="Recule", command=self.move_backward)
        self.backward_button.pack(fill=tk.X)
        
        self.left_button = tk.Button(self, text="Gauche", command=self.move_left)
        self.left_button.pack(fill=tk.X)
        
        self.right_button = tk.Button(self, text="Droite", command=self.move_right)
        self.right_button.pack(fill=tk.X)
        
        self.linear_speed_label = tk.Label(self, text="Vitesse:")
        self.linear_speed_label.pack()
        
        self.linear_speed_slider = tk.Scale(self, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL)
        self.linear_speed_slider.pack(fill=tk.X)
        
        self.angular_speed_label = tk.Label(self, text="Vitesse de rotation:")
        self.angular_speed_label.pack()
        
        self.angular_speed_slider = tk.Scale(self, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL)
        self.angular_speed_slider.pack(fill=tk.X)
        
    def move_forward(self):
        linear_speed = self.linear_speed_slider.get()
        self.robot_controller.move(linear_speed, 0, 1)
        
    def move_backward(self):
        linear_speed = -self.linear_speed_slider.get()
        self.robot_controller.move(linear_speed, 0, 1)
        
    def move_left(self):
        angular_speed = self.angular_speed_slider.get()
        self.robot_controller.move(0, angular_speed, 1)
        
    def move_right(self):
        angular_speed = -self.angular_speed_slider.get()
        self.robot_controller.move(0, angular_speed, 1)
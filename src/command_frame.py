import tkinter as tk

class CommandFrame(tk.Frame):
    def __init__(self, parent, robot_controller):
        super().__init__(parent)
        self.robot_controller = robot_controller
        
        self.forward_button = tk.Button(self, text="Forward", command=self.move_forward)
        self.forward_button.pack(fill=tk.X)
        
        self.backward_button = tk.Button(self, text="Backward", command=self.move_backward)
        self.backward_button.pack(fill=tk.X)
        
        self.left_button = tk.Button(self, text="Left", command=self.move_left)
        self.left_button.pack(fill=tk.X)
        
        self.right_button = tk.Button(self, text="Right", command=self.move_right)
        self.right_button.pack(fill=tk.X)
        
        self.linear_speed_label = tk.Label(self, text="Linear Speed:")
        self.linear_speed_label.pack()
        
        self.linear_speed_slider = tk.Scale(self, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL)
        self.linear_speed_slider.pack(fill=tk.X)
        
        self.angular_speed_label = tk.Label(self, text="Angular Speed:")
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
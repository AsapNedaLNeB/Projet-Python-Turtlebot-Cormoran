import tkinter as tk
from tkinter import messagebox

class ConnectionFrame(tk.Frame):
    def __init__(self, parent, robot_controller):
        super().__init__(parent)

        self.robot_controller = robot_controller
        
        self.master_uri_label = tk.Label(self, text="ROS Master URI:")
        self.master_uri_label.pack(side=tk.LEFT)
        
        self.master_uri_entry = tk.Entry(self)
        self.master_uri_entry.pack(side=tk.LEFT)
        
        self.hostname_label = tk.Label(self, text="Hostname:")
        self.hostname_label.pack(side=tk.LEFT)
        
        self.hostname_entry = tk.Entry(self)
        self.hostname_entry.pack(side=tk.LEFT)
        
        self.start_button = tk.Button(self, text="Start", command=self.start_connection)
        self.start_button.pack(side=tk.LEFT)
        
        self.stop_button = tk.Button(self, text="Stop", command=self.stop_connection)
        self.stop_button.pack(side=tk.LEFT)
        
        self.connection_status = tk.Label(self, text="Disconnected", fg="red")
        self.connection_status.pack(side=tk.LEFT)
        
    def start_connection(self):
        master_uri = self.master_uri_entry.get()
        hostname = self.hostname_entry.get()
        # Logic to start connection to the robot
        # For now, we just simulate a successful connection
        self.connection_status.config(text="Connected", fg="green")
        messagebox.showinfo("Connection", "Connected to the robot")
        
    def stop_connection(self):
        # Logic to stop connection to the robot
        # For now, we just simulate a successful disconnection
        self.connection_status.config(text="Disconnected", fg="red")
        messagebox.showinfo("Connection", "Disconnected from the robot")
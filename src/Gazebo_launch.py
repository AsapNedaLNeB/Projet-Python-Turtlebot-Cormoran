# Ce programme lance gazebo automatiquement

import subprocess
import time
import os

class GazeboLauncher:

    def __init__(self, ros_setup_path="/opt/ros/melodic/setup.bash", catkin_setup_path="~/catkin_ws/devel/setup.bash", turtlebot_model="burger"):

        # Initialise les chemins d'accès pour les configurations ROS et catkin, et le modèle de Turtlebot
        self.ros_setup_path = ros_setup_path
        self.catkin_setup_path = catkin_setup_path
        self.turtlebot_model = turtlebot_model

        # Initialise les variables de processus
        self.roscore_process = None
        self.gazebo_process = None
        self.teleop_process = None

    def setup_environment(self):
        # Source les configurations ROS et catkin
        os.system(f"source {self.ros_setup_path}")
        os.system(f"source {self.catkin_setup_path}")
        
        # Définit le modèle de Turtlebot dans les variables d'environnement
        os.environ['TURTLEBOT3_MODEL'] = self.turtlebot_model

    def launch_roscore(self):
        # Lance roscore dans un nouveau terminal
        self.roscore_process = subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'roscore'])

    def launch_gazebo(self):
        # Lance Gazebo avec un monde vide dans un nouveau terminal
        self.gazebo_process = subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch'])

    def launch_teleop(self):
        # Lance teleop pour le contrôle du Turtlebot au clavier dans un nouveau terminal
        self.teleop_process = subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch'])

    def launch(self):
        # Configure l'environnement et lance roscore, Gazebo et teleop
        self.setup_environment()
        self.launch_roscore()
        
        # Attends le démarrage de roscore (ajuster le temps d'attente si nécessaire)
        time.sleep(3)

        # Lance Gazebo et teleop
        self.launch_gazebo()
        self.launch_teleop()

    # Termine tous les processus lancés
    def terminate_processes(self):
        if self.roscore_process:
            self.roscore_process.terminate()
        if self.gazebo_process:
            self.gazebo_process.terminate()
        if self.teleop_process:
            self.teleop_process.terminate()
        print("Processes terminated.")

if __name__ == "__main__":
    # Crée une instance de GazeboLauncher et lance les processus
    launcher = GazeboLauncher()
    launcher.launch()

    try:
        # Maintient le script actif jusqu'à une interruption clavier (Ctrl+C)
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Termine les processus proprement en cas d'interruption
        launcher.terminate_processes()
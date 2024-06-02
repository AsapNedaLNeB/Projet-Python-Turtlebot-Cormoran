#lance gazebo automatiquement

import subprocess # librairie permettant d'ouvrir plusieurs terminaux en même temps 
import time
import os

def launch_gazebo():
    os.system("source /opt/ros/melodic/setup.bash")
    os.system("source ~/catkin_ws/devel/setup.bash")  # à modifier suivant l'emplacement du dosier catkin_ws

    os.environ['TURTLEBOT3_MODEL'] = 'burger'  # défini le modèle de bot

    # démarre roscore
    roscore_process = subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'roscore'])
    
    # Attends le démarrage de roscore pour démarrer la suite (besoin d'augmenter le sleep() si ordinateur trop lent)
    time.sleep(3)

    # Lance Gazebo dans un monde vide
    gazebo_process = subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch'])

    # Lance teleop pour le controle clavier
    teleop_process = subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch'])

    return roscore_process, gazebo_process, teleop_process

if __name__ == "__main__":
    roscore_process, gazebo_process, teleop_process = launch_gazebo()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        roscore_process.terminate()
        gazebo_process.terminate()
        teleop_process.terminate()
        print("Processes terminated.")

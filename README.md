## Projet-Python-Turtlebot-Cormoran

repo github du code du projet python Turtlebot3 groupe Cormoran

Lien : https://github.com/AsapNedaLNeB/Projet-Python-Turtlebot-Cormoran

## Contributeurs:

Pierre Peaupardin
Thibaut Barottin
Vlad Tondeur
Nicolas Notter

## Description
Une application Python avec interface graphique pour contrôler un robot TurtleBot sur gazebo. L'application permet de simuler le robot, visualiser ses mouvements, et commander ses déplacements.

## Structure
- `main.py`
- `movement_frame.py`: Affichage des mouvements du robot.
- `command_frame.py`: Commandes pour déplacer le robot.
- `robot_controller.py`: Interface gazebo pour contrôler le robot.
- `Gazebo_launch` : Lance gazebo 

## Exécution

1. Exécutez l'application python : main.py (oui c'est tout)

## Requirements
Utiliser sur Ubuntu

Installation valide de ROS Melodic et de gazebo

Setup du dossier catkin_ws avec la simulation (voir lien 1)

avoir executé dans le terminal (pour ubuntu):

-`$ sudo apt-get install python-geometry-msgs`

-`$ sudo apt-get install python-nav_msgs`

-`$ sudo apt-get install ros-melodic-rospy`

Voir `setup.py` pour les packages necessaires

## Liens
1) Pour setup gazebo avec ROS: https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/
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

1. Exécutez l'application python : main.py

## Utilisation

Contrôle du déplacement avec z,q,s,d ou les boutons du GUI (vitesse de déplacement avec les boutons gérée par les sliders, à 0 le robot reste immobile)

La fenêtre du GUI ne doit PAS être en arrière plan

NB: De gros lags sont présents sur le GUI qui ont de gros impacts sur la simulation, source inconnue

## Requirements
Utiliser sur Ubuntu

Installation valide de ROS Melodic (cf lien 1) et de Gazebo 

Setup du dossier catkin_ws avec la simulation (cf lien 2) dans le dossier home (sinon modifier le chemin d'accès dans `Gazebo_launch.py`, ligne 9)

avoir executé dans le terminal (pour ubuntu):

- `$ sudo apt-get install python-geometry-msgs`

- `$ sudo apt-get install python-nav_msgs`

- `$ sudo apt-get install ros-melodic-rospy`

Voir `setup.py` ou `pyproject.toml` pour les packages necessaires, sinon faire `pip install -e .` dans la console python

## Liens
Github : https://github.com/AsapNedaLNeB/Projet-Python-Turtlebot-Cormoran

1) Pour installer ROS : https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/

2) Pour setup gazebo avec ROS: https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/ 

     (uniquement la partie 1.1.1 est nécessaire, le reste est géré par `Gazebo_launch.py`)

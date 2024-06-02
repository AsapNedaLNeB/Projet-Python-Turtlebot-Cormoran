
#code permettant d'installer les packages nécessaires au bon fonctionnement de l'app
from setuptools import setup, find_packages

setup(
    name='turtlebot_controller',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'tk',
        'matplotlib',
        #'rospy', à installer à la main dans le terminal
        #'geometry_msgs',
        #'nav_msgs',
    ],
)

from setuptools import setup, find_packages

setup(
    name='turtlebot_controller',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'tkinter',
        'matplotlib',
        'rospy',
        'geometry_msgs',
        'nav_msgs',
    ],
)
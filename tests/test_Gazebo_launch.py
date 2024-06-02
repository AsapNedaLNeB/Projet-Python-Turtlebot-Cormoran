# Ce programme test Gazebo_launch.py, qui lance gazebo automatiquement

import pytest
from unittest.mock import patch, MagicMock
import os
import subprocess
import time
from Gazebo_launch import GazeboLauncher  

@pytest.fixture
def gazebo_launcher():
    launcher = GazeboLauncher()
    return launcher

# Test pour vérifier que les processus impliqués dans le projet se lancent bien comme il faut

@patch('subprocess.Popen')
def test_launch_roscore(mock_popen, gazebo_launcher):
    mock_popen.return_value = MagicMock()
    gazebo_launcher.launch_roscore()
    mock_popen.assert_called_with(['gnome-terminal', '--', 'bash', '-c', 'roscore'])
    assert gazebo_launcher.roscore_process is not None

@patch('subprocess.Popen')
def test_launch_gazebo(mock_popen, gazebo_launcher):
    mock_popen.return_value = MagicMock()
    gazebo_launcher.launch_gazebo()
    mock_popen.assert_called_with(['gnome-terminal', '--', 'bash', '-c', 'roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch'])
    assert gazebo_launcher.gazebo_process is not None

@patch('subprocess.Popen')
def test_launch_teleop(mock_popen, gazebo_launcher):
    mock_popen.return_value = MagicMock()
    gazebo_launcher.launch_teleop()
    mock_popen.assert_called_with(['gnome-terminal', '--', 'bash', '-c', 'roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch'])
    assert gazebo_launcher.teleop_process is not None

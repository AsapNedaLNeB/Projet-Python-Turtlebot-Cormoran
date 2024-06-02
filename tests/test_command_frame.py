# Ce programme sert de test à command_frame.py, qui gère le controle du turtlebot

import pytest
from unittest.mock import MagicMock
import tkinter as tk
from command_frame import CommandFrame  

@pytest.fixture
def command_frame():
    root = tk.Tk()
    robot_controller = MagicMock()
    frame = CommandFrame(root, robot_controller)
    yield frame
    root.destroy()

# Tests des commandes de mouvement

def test_move_forward(command_frame):
    command_frame.linear_speed_slider.set(0.5)
    command_frame.move_forward()
    command_frame.robot_controller.move.assert_called_with(0.5, 0, 1)

def test_move_backward(command_frame):
    command_frame.linear_speed_slider.set(0.5)
    command_frame.move_backward()
    command_frame.robot_controller.move.assert_called_with(-0.5, 0, 1)

def test_move_left(command_frame):
    command_frame.angular_speed_slider.set(0.5)
    command_frame.move_left()
    command_frame.robot_controller.move.assert_called_with(0, 0.5, 1)

def test_move_right(command_frame):
    command_frame.angular_speed_slider.set(0.5)
    command_frame.move_right()
    command_frame.robot_controller.move.assert_called_with(0, -0.5, 1)


# Tests d'initialisation des boutons et des sliders


def test_buttons_initialization(command_frame):
    assert isinstance(command_frame.forward_button, tk.Button)
    assert isinstance(command_frame.backward_button, tk.Button)
    assert isinstance(command_frame.left_button, tk.Button)
    assert isinstance(command_frame.right_button, tk.Button)

def test_sliders_initialization(command_frame):
    assert isinstance(command_frame.linear_speed_slider, tk.Scale)
    assert isinstance(command_frame.angular_speed_slider, tk.Scale)
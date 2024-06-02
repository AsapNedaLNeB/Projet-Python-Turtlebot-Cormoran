# Ce programme test celui qui gère la partie graph de l'interface graphique, movement_frame.py

import pytest
from unittest.mock import MagicMock, patch
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from movement_frame import MovementFrame  

@pytest.fixture
def movement_frame():
    root = tk.Tk()
    robot_controller = MagicMock()
    robot_controller.current_pose = MagicMock()
    frame = MovementFrame(root, robot_controller)
    yield frame
    root.destroy()

# Tests qui s'assurent de la mise à jour périodique des graphiques dynamiques

@patch('movement_frame.MovementFrame.update_graph')
def test_update_graph_call(mock_update_graph, movement_frame):
    movement_frame.ani.event_source.start()
    mock_update_graph.assert_called()


def test_update_graph_data(movement_frame):
    movement_frame.robot_controller.current_pose.position.x = 1.0
    movement_frame.robot_controller.current_pose.position.y = 1.0
    
    movement_frame.update_graph(0)
    
    x_data = movement_frame.line_position.get_xdata()
    y_data = movement_frame.line_position.get_ydata()
    speed_data = movement_frame.line_velocity.get_ydata()
    
    assert x_data[-1] == 1.0
    assert y_data[-1] == 1.0
    assert np.isclose(speed_data[-1], np.sqrt(2.0))

# Vérifie que les axes se mettent correctement à jour en fonction des nouvelles données reçues (pas de courbe qui sort du cadre)

def test_update_graph_scaling(movement_frame):
    movement_frame.robot_controller.current_pose.position.x = 10.0
    movement_frame.robot_controller.current_pose.position.y = 10.0
    
    movement_frame.update_graph(0)
    
    y_lim = movement_frame.ax[1].get_ylim()
    
    assert y_lim[1] >= np.sqrt(200)

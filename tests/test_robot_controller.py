# Ce programme test robot_controller.py, qui gère la simulation du turtlebot

import pytest
from unittest.mock import MagicMock, patch
from geometry_msgs.msg import Twist, Pose
from nav_msgs.msg import Odometry
import rospy
from robot_controller import TurtleBot3Controller  

@pytest.fixture
def turtlebot_controller():
    with patch('rospy.init_node'), patch('rospy.Publisher'), patch('rospy.Subscriber'), patch('rospy.sleep'):
        controller = TurtleBot3Controller()
    return controller

# Test qui vérifie que le callback met correctement à jour la pose actuelle

def test_odom_callback(turtlebot_controller):
    pose = Pose()
    pose.position.x = 1.0
    pose.position.y = 2.0
    odom = Odometry()
    odom.pose.pose = pose
    
    turtlebot_controller.odom_callback(odom)
    
    assert turtlebot_controller.current_pose == pose

# Test qui vérifie que les commandes de mouvement sont correctement publiées avec les bons paramètres, et que le robot s'arrête après la durée spécifiée

@patch('rospy.Rate')
def test_move(mock_rate, turtlebot_controller):
    mock_rate.return_value = MagicMock()
    turtlebot_controller.cmd_vel_pub = MagicMock()
    
    turtlebot_controller.move(0.5, 0.1, 2)
    
    assert turtlebot_controller.cmd_vel_pub.publish.call_count == 21                            # 20 pour la durée + 1 pour le temps de la commande de stop
    first_call = turtlebot_controller.cmd_vel_pub.publish.call_args_list[0]
    last_call = turtlebot_controller.cmd_vel_pub.publish.call_args_list[-1]
    
    assert isinstance(first_call[0][0], Twist)
    assert first_call[0][0].linear.x == 0.5
    assert first_call[0][0].angular.z == 0.1
    assert last_call[0][0].linear.x == 0.0
    assert last_call[0][0].angular.z == 0.0
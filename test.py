import rospy
from robot_controler import TurtleBotController

if __name__ == "__main__":
    rospy.init_node('turtlebot_gui')
    controller= TurtleBotController()
    controller.run()
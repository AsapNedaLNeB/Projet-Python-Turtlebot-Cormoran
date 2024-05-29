import rospy
from controller import TurtleBotController

if __name__ == "__main__":
    rospy.init_node('turtlebot_gui')
    controller= TurtleBotController()
    controller.run()
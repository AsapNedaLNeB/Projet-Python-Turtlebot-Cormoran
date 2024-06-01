#gère la simulation du turtlebot

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

class TurtleBot3Controller:
    def __init__(self):
        rospy.init_node('turtlebot3_controller', anonymous=True)
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.odom_sub = rospy.Subscriber('/odom', Odometry, self.odom_callback)
        self.current_pose = None
        rospy.sleep(1)  # attente de l'initialisation

    def odom_callback(self, msg):
        self.current_pose = msg.pose.pose
        #rospy.loginfo_throttle(1, f"Current pose: {self.current_pose}")  # log console

    def move(self, linear_speed=0.0, angular_speed=0.0, duration=1):
        move_cmd = Twist()
        move_cmd.linear.x = linear_speed
        move_cmd.angular.z = angular_speed
        rate = rospy.Rate(10)  # fréquence d'actualisation de l'entrée

        for _ in range(int(duration * 10)):  # ajustement à la fréquence
            self.cmd_vel_pub.publish(move_cmd)
            rate.sleep()

        # Stop le robot une fois son mouvement effectué
        move_cmd.linear.x = 0.0
        move_cmd.angular.z = 0.0
        self.cmd_vel_pub.publish(move_cmd)
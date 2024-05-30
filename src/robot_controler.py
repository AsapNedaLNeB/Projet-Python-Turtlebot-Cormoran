import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

class RobotController:
    def __init__(self):
        rospy.init_node('robot_controller', anonymous=True)
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.odom_sub = rospy.Subscriber('/odom', Odometry, self.odom_callback)
        self.current_pose = None

    def odom_callback(self, msg):
        self.current_pose = msg.pose.pose

    def send_velocity_command(self, linear, angular):
        twist = Twist()
        twist.linear.x = linear
        twist.angular.z = angular
        self.cmd_vel_pub.publish(twist)

    def stop(self):
        self.send_velocity_command(0, 0)
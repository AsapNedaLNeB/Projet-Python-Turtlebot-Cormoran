import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

class TurtleBot3Controller:
    def __init__(self):
        rospy.init_node('turtlebot3_controller', anonymous=True)
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.odom_sub = rospy.Subscriber('/odom', Odometry, self.odom_callback)
        self.current_pose = None
        rospy.sleep(1)  # Wait for subscribers and publishers to initialize

    def odom_callback(self, msg):
        self.current_pose = msg.pose.pose
        #rospy.loginfo(f"Current pose: {self.current_pose}")

    def move(self, linear_speed=0.0, angular_speed=0.0, duration=1.0):
        move_cmd = Twist()
        move_cmd.linear.x = linear_speed
        move_cmd.angular.z = angular_speed
        rate = rospy.Rate(5)  # 5 Hz

        for _ in range(int(duration * 10)):  # Duration in seconds
            self.cmd_vel_pub.publish(move_cmd)
            rate.sleep()

        # Stop the robot
        move_cmd.linear.x = 0.0
        move_cmd.angular.z = 0.0
        self.cmd_vel_pub.publish(move_cmd)
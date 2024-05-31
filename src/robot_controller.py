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
        #rospy.loginfo_throttle(1, f"Current pose: {self.current_pose}")  # Throttled logging

    def move(self, linear_speed=0.0, angular_speed=0.0, duration=1):
        move_cmd = Twist()
        move_cmd.linear.x = linear_speed
        move_cmd.angular.z = angular_speed
        rate = rospy.Rate(10)  # Set rate to 10 Hz

        for _ in range(int(duration * 10)):  # Adjust loop count for 10 Hz rate
            self.cmd_vel_pub.publish(move_cmd)
            rate.sleep()

        # Stop the robot after the movement
        move_cmd.linear.x = 0.0
        move_cmd.angular.z = 0.0
        self.cmd_vel_pub.publish(move_cmd)

if __name__ == "__main__":
    controller = TurtleBot3Controller()
    
    try:
        while not rospy.is_shutdown():
            # Example move commands
            controller.move(0.2, 0.0, 2.0)  # Move forward at 0.2 m/s for 2 seconds
            controller.move(0.0, 0.5, 4.0)  # Rotate at 0.5 rad/s for 4 seconds
    except rospy.ROSInterruptException:
        pass
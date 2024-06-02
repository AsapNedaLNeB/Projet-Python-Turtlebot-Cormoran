# Ce programme gère la simulation du turtlebot

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

class TurtleBot3Controller:
    def __init__(self):
        # Initialise le noeud ROS pour le contrôleur TurtleBot3
        rospy.init_node('turtlebot3_controller', anonymous=True)

        # Initialise le publisher pour la commande de vitesse
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        # Initialise le subscriber pour la position
        self.odom_sub = rospy.Subscriber('/odom', Odometry, self.odom_callback)

        # Initialise la variable de la position actuelle
        self.current_pose = None

        # Attente d'une seconde pour l'initialisation
        rospy.sleep(1)

    def odom_callback(self, msg):
        # Callback pour mettre à jour la position actuelle
        self.current_pose = msg.pose.pose

        # Log de la pose actuelle avec une fréquence de 1 Hz
        rospy.loginfo_throttle(1, f"Current pose: {self.current_pose}")

    def move(self, linear_speed=0.0, angular_speed=0.0, duration=1):
        # Initialise la commande de mouvement
        move_cmd = Twist()
        move_cmd.linear.x = linear_speed
        move_cmd.angular.z = angular_speed
        
        # Définit la fréquence de mise à jour
        rate = rospy.Rate(10)  # 10 Hz

        # Boucle pour publier la commande pendant la durée spécifiée
        for _ in range(int(duration * 10)):  # Convertit la durée en nombre de cycles à la fréquence donnée
            self.cmd_vel_pub.publish(move_cmd)
            rate.sleep()

        # Arrête le robot une fois le mouvement effectué
        move_cmd.linear.x = 0.0
        move_cmd.angular.z = 0.0
        self.cmd_vel_pub.publish(move_cmd)
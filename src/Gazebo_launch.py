import subprocess
import time
import os

def launch_gazebo():
    # Source the ROS setup.bash files
    os.system("source /opt/ros/melodic/setup.bash")
    os.system("source ~/catkin_ws/devel/setup.bash")  # Adjust if your catkin workspace is different

    # Export necessary environment variables
    os.environ['TURTLEBOT3_MODEL'] = 'burger'  # Adjust if using a different model

    # Launch roscore
    roscore_process = subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'roscore'])
    
    # Wait for roscore to start
    time.sleep(5)

    # Launch Gazebo with TurtleBot3 world
    gazebo_process = subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'roslaunch turtlebot3_gazebo turtlebot3_world.launch'])

    # Launch teleop_keyboard (optional for manual control)
    teleop_process = subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch'])

    return roscore_process, gazebo_process, teleop_process

if __name__ == "__main__":
    roscore_process, gazebo_process, teleop_process = launch_gazebo()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        roscore_process.terminate()
        gazebo_process.terminate()
        teleop_process.terminate()
        print("Processes terminated.")

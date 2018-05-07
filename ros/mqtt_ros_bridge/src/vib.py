#!/usr/bin/python

from nav_msgs.msg import Odometry
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
import bridge
import rospy
import signal

global posX
global vel

posX=0.0
vel = ""
def callback_vib(data):
    global vel
    global posX
 
    pose = PoseStamped()
    pose.header.frame_id = "odom"
    x = float(data.pose.pose.position.x)
    
    if x>(posX+0.01):
        posX = x
	y = float(data.pose.pose.position.y)
	rospy.loginfo("%s", y)
	if y < 0.03 and y > -0.03:
		vel = "0"
	elif y > 0.03 and y < 0.1:
		vel = "3D"
	elif y > 0.1 and y < 0.2:
		vel ="2D"
	elif y > 0.2:
		vel="1D"
	elif y < -0.03 and y > -0.1:
                vel = "3S"
        elif y < -0.1 and y > -0.2:
                vel ="2S"
        elif y < -0.2:
                vel="1S"


def main():
    global vel
    global v
    v=""
    rospy.init_node('vib_feedback', anonymous=True)
    vib_subscriber =  rospy.Subscriber('/odom', Odometry, callback_vib)
    vib_publisher = rospy.Publisher('/vibration_vel', String, queue_size=1)
    while not rospy.is_shutdown():
	if (vel == "1D" or vel == "2D" or vel=="3D" or vel=="0" or vel == "1S" or vel == "2S" or vel=="3S")and v!=vel:
    		vib_publisher.publish(vel)
		v = vel
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

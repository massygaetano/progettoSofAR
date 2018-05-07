#!/usr/bin/python

from sensor_msgs.msg import Imu
from geometry_msgs.msg import Vector3
from std_msgs.msg import String
import bridge
import rospy
import signal

global bool
bool=False

class imu_bridge(bridge.bridge):

    def msg_process(self, msg):
 	msg_list = msg.split(";")

        acceleration = Vector3()
        acceleration.x = float(msg_list[1].replace(',','.'))
        acceleration.y = float(msg_list[2].replace(',','.'))
        acceleration.z = float(msg_list[3].replace(',','.'))

        velocity = Vector3()
        velocity.x = float(msg_list[5].replace(',','.'))
        velocity.y = float(msg_list[6].replace(',','.'))
        velocity.z = float(msg_list[7].replace(',','.'))

        imu_message = Imu()
        now = rospy.get_rostime()
        imu_message.header.stamp.secs = now.secs
        imu_message.header.stamp.nsecs = now.nsecs
        imu_message.header.frame_id = "0"
        imu_message.linear_acceleration = acceleration
        imu_message.angular_velocity = velocity

        return imu_message

def callback_vib(data):
    rospy.loginfo("%s", data.data)
    global vel
    vel = data.data
    global  bool
    bool = True

def main():
    global bool
    rospy.init_node('imu_bridge', anonymous=True)
    imu_publisher = rospy.Publisher('/imu_data', String, queue_size=1)
    vib_subscriber =  rospy.Subscriber('/vibration_vel', String, callback_vib)
    vib_sub = imu_bridge(imu_publisher, "vibration/vel")
    rospy.on_shutdown(vib_sub.hook)
    while not rospy.is_shutdown():
       vib_sub.looping()
       if bool:
	 bool=False
         global vel
      	 vib_sub.pub(vel)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

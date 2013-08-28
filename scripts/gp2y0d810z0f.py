#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import Adafruit_BBIO.GPIO as GPIO

# Sensor connected to P8_14

def GP2Y0D810Z0F():
    GPIO.setup("P8_14", GPIO.IN)
    pub = rospy.Publisher('ir_sharp_10cm', String)
    rospy.init_node('gp2y0d810z0f')
    r = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        if GPIO.input("P8_14"):
            r.sleep()
        else:
            cad = "GP2Y0D810Z0F (10cm): object detected" 
            rospy.loginfo(cad)
            pub.publish(String(measure))
            #rospy.sleep(1.0)
            r.sleep()

if __name__ == '__main__':
    try:
        GP2Y0D810Z0F()
    except rospy.ROSInterruptException:
        pass


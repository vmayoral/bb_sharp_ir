#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import Adafruit_BBIO.ADC as ADC


def gp2y0a12():
    ADC.setup()
    pub = rospy.Publisher('gp2y0a12_raw', String)
    rospy.init_node('gp2y0a12_node')
    r = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        str = "gp2y0a12: %s" % rospy.get_time()
        rospy.loginfo(str)
        pub.publish(String(str))
        #rospy.sleep(1.0)
        r.sleep()


if __name__ == '__main__':
    try:
        gp2y0a12()
    except rospy.ROSInterruptException:
        pass

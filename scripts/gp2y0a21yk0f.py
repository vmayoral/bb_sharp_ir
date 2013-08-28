#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import Adafruit_BBIO.ADC as ADC

# Sensor connected to P9_40

def gp2y0a12():
    ADC.setup()
    pub = rospy.Publisher('ir_sharp_80cm', String)
    rospy.init_node('gp2y0a21yk0f')
    r = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        measure = str(ADC.read_raw("P9_40"))
        cad = "gp2y0a12: %s" % measure
        rospy.loginfo(cad)
        pub.publish(String(measure))
        #rospy.sleep(1.0)
        r.sleep()


if __name__ == '__main__':
    try:
        gp2y0a12()
    except rospy.ROSInterruptException:
        pass


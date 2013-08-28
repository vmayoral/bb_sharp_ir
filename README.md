bb_sharp_ir
==========

![Sharp GP2Y0A21 Distance Sensor (10-80cm)](http://www.dfrobot.com/image/cache/data/SEN0014/SEN0014-340x340.jpg)

![Sharp GP2Y0D810Z0F Distance Sensor](http://www.ec.in.th/image/cache/data/Sensors/GP2Y0D810Z0F-500x500.jpg)

This ROS package publishes the Sharp IR sensors values to a ROS topic. For now the following sensors are supported:

* GP2Y0A21 Distance Sensor (10-80cm) [`scripts/GP2Y0A21YK0F.py`]

* GP2Y0D810Z0F Digital Distance Sensor (10cm) [`scripts/GP2Y0D810Z0F.py`]

* GP2Y0D805Z0F Digital Distance Sensor (5cm) [`scripts/GP2Y0D805Z0F.py`]

-----------

Note that this package makes use of the [adafruit-beaglebone-io-python](https://github.com/adafruit/adafruit-beaglebone-io-python) library.

---------

####[gp2y0a21yk0f](https://github.com/vmayoral/bb_sharp_ir/blob/master/scripts/gp2y0a21yk0f.py)
ROS node that reads a Sharp IR gp2y0a21yk0f sensor (analog sensor) and publishes its output to a topic. The code is configured so that the sensor is connected to P9_40. (Needs to use ADC). The information published can be interpreted as distance. The sensor is able to recognize objects from 10cm to 80cm.
#####Published topics
*ir_sharp_80cm (std_msgs.msg String)*


####[gp2y0d805z0f](https://github.com/vmayoral/bb_sharp_ir/blob/master/scripts/gp2y0d805z0f.py)
ROS node that reads a Sharp IR gp2y0d805z0f sensor (digital sensor) and publishes its output to a topic. The code is configured so that the sensor is connected to the Beaglebone P8_14. The node publishes whether the sensor detects and object within its range (5 cm).
#####Published topics
*ir_sharp_5cm (std_msgs.msg String)*

####[gp2y0d810z0f](https://github.com/vmayoral/bb_sharp_ir/blob/master/scripts/gp2y0d810z0f.py)
ROS node that reads a Sharp IR gp2y0d810z0f sensor (digital sensor) and publishes its output to a topic. The code is configured so that the sensor is connected to the Beaglebone P8_14. The node publishes whether the sensor detects and object within its range (10 cm).
#####Published topics
*ir_sharp_10cm (std_msgs.msg String)*

cmake_minimum_required(VERSION 2.8.3)
project(bb_sharp_ir)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS rospy std_msgs)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES bb_sharp_IR
  CATKIN_DEPENDS rospy std_msgs
#  DEPENDS system_lib
)

include_directories(include
    ${catkin_INCLUDE_DIRS}
)

install(PROGRAMS scripts/GP2Y0A21YK0F.py scripts/GP2Y0D810Z0F.py scripts/GP2Y0D805Z0F.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})


cmake_minimum_required(VERSION 2.8.3)
project(katana_arm_gazebo)

find_package(catkin REQUIRED COMPONENTS roscpp actionlib control_msgs)


catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES package_example
#  CATKIN_DEPENDS roscpp rospy sensor_msgs
#  DEPENDS system_lib
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(min_max_trajectory src/min_max_trajectory.cpp)

target_link_libraries(min_max_trajectory
   ${catkin_LIBRARIES}
)


install(TARGETS min_max_trajectory
   ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
   LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
   RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)


cmake_minimum_required(VERSION 2.8.3)
project(katana_joint_movement_adapter)

find_package(catkin REQUIRED COMPONENTS roscpp rospy sensor_msgs actionlib urdf)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES package_example
#  CATKIN_DEPENDS roscpp rospy sensor_msgs
#  DEPENDS system_lib
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

add_executable(joint_movement_adapter src/joint_movement_adapter.cpp)


target_link_libraries(joint_movement_adapter
  ${catkin_LIBRARIES}
)


install(TARGETS joint_movement_adapter
  ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

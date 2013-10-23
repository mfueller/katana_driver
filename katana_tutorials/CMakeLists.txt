cmake_minimum_required(VERSION 2.8.3)
project(katana_tutorials)

find_package(catkin REQUIRED COMPONENTS roscpp rospy sensor_msgs actionlib moveit_msgs )
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

add_executable(follow_joint_trajectory_client src/follow_joint_trajectory_client.cpp)
add_executable(katana_joint_trajectory_client src/katana_joint_trajectory_client.cpp)

target_link_libraries(follow_joint_trajectory_client
   ${catkin_LIBRARIES}
)

target_link_libraries(katana_joint_trajectory_client
   ${catkin_LIBRARIES}
)

install(TARGETS follow_joint_trajectory_client katana_joint_trajectory_client
  ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)


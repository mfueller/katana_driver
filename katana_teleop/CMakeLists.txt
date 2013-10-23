cmake_minimum_required(VERSION 2.8.3)
project(katana_teleop)

find_package(catkin REQUIRED COMPONENTS roscpp rospy sensor_msgs actionlib)

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


add_executable(katana_teleop_key src/katana_teleop_key.cpp) 
add_executable(katana_teleop_ps3 src/katana_teleop_ps3joy.cpp)
add_executable(katana_teleop_cyborgevo src/katana_teleop_cyborgevo.cpp)

target_link_libraries(katana_teleop_key
  ${catkin_LIBRARIES}
)
target_link_libraries(katana_teleop_ps3
  ${catkin_LIBRARIES}
)
target_link_libraries(katana_teleop_cyborgevo
  ${catkin_LIBRARIES}
)

install(TARGETS katana_teleop_key katana_teleop_ps3 katana_teleop_cyborgevo
  ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)


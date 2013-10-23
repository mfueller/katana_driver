cmake_minimum_required(VERSION 2.8.3)
project(katana)

find_package(catkin REQUIRED COMPONENTS roscpp sensor_msgs kni tf katana_msgs actionlib urdf roslib)


catkin_package(
  INCLUDE_DIRS include
  CATKIN_DEPENDS roscpp kni tf katana_msgs actionlib
)


include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

set(KNI_LIB_DIR "${kni_SOURCE_DIR}/KNI_4.3.0/lib/linux")

link_directories( ${KNI_LIB_DIR} )

add_executable(katana 
  src/KatanaNode.cpp 
  src/AbstractKatana.cpp 
  src/Katana.cpp src/Katana300.cpp 
  src/SimulatedKatana.cpp 
  src/JointStatePublisher.cpp 
  src/joint_trajectory_action_controller.cpp 
  src/joint_movement_action_controller.cpp 
  src/KNIConverter.cpp 
  src/spline_functions.cpp 
  src/katana_gripper_grasp_controller.cpp
)

add_executable(katana_arm_kinematics 
  src/KNIConverter.cpp 
  src/KNIKinematics.cpp
)


target_link_libraries(katana
   ${catkin_LIBRARIES}
   Kinematics
   KNIBase
   KNI_InvKin
   KNI_LM
)

target_link_libraries(katana_arm_kinematics
   ${catkin_LIBRARIES}
   Kinematics
   KNIBase
   KNI_InvKin
   KNI_LM
)


install(TARGETS katana katana_arm_kinematics
   ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
   LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
   RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)


install(DIRECTORY include/${PROJECT_NAME}/
   DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
   FILES_MATCHING PATTERN "*.h"
)


install(FILES
  launch/katana_300_6m180.launch  
  launch/katana_400_6m180.launch  
  launch/katana_450_6m90a.launch  
  launch/katana_450_6m90b.launch  
  launch/katana_arm_kinematics.launch  
  launch/katana.launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)


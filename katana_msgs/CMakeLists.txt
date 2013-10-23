cmake_minimum_required(VERSION 2.8.3)
project(katana_msgs)

find_package(catkin REQUIRED COMPONENTS roscpp message_generation actionlib sensor_msgs)

add_message_files(
   FILES
   GripperControllerState.msg
)

add_action_files(
  DIRECTORY action
  FILES
  JointMovement.action
)

generate_messages(
   DEPENDENCIES
   actionlib_msgs std_msgs sensor_msgs
)



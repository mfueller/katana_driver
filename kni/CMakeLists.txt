cmake_minimum_required(VERSION 2.8.3)
project(kni)

find_package(catkin REQUIRED COMPONENTS roscpp)

catkin_package(
  INCLUDE_DIRS KNI_4.3.0/include
#  LIBRARIES package_example
#  CATKIN_DEPENDS roscpp rospy sensor_msgs
#  DEPENDS system_lib
)

include_directories(
  KNI_4.3.0/include
  ${catkin_INCLUDE_DIRS}
)

execute_process(COMMAND cmake -E chdir ${PROJECT_SOURCE_DIR}/KNI_4.3.0/src/common/ make
                RESULT_VARIABLE _make_failed)
if(_make_failed)
  message(FATAL_ERROR "Build of common files failed")
endif(_make_failed)

execute_process(COMMAND cmake -E chdir ${PROJECT_SOURCE_DIR}/KNI_4.3.0/src/Base/ make
                RESULT_VARIABLE _make_failed)
if(_make_failed)
  message(FATAL_ERROR "Build of Base library failed")
endif(_make_failed)

execute_process(COMMAND cmake -E chdir ${PROJECT_SOURCE_DIR}/KNI_4.3.0/lib/kinematics/roboop/ make
                RESULT_VARIABLE _make_failed)
if(_make_failed)
  message(FATAL_ERROR "Build of roboop library failed")
endif(_make_failed)

execute_process(COMMAND cmake -E chdir ${PROJECT_SOURCE_DIR}/KNI_4.3.0/lib/kinematics/ make
                RESULT_VARIABLE _make_failed)
if(_make_failed)
  message(FATAL_ERROR "Build of kinematics library failed")
endif(_make_failed)

execute_process(COMMAND cmake -E chdir ${PROJECT_SOURCE_DIR}/KNI_4.3.0/src/InvKin/ make
                RESULT_VARIABLE _make_failed)
if(_make_failed)
  message(FATAL_ERROR "Build of InvKin library failed")
endif(_make_failed)

execute_process(COMMAND cmake -E chdir ${PROJECT_SOURCE_DIR}/KNI_4.3.0/src/LM/ make
                RESULT_VARIABLE _make_failed)
if(_make_failed)
  message(FATAL_ERROR "Build of LM library failed")
endif(_make_failed)



install(#TARGETS 
  FILES KNI_4.3.0/lib/linux/libKinematics.so KNI_4.3.0/lib/linux/libKinematics.a
  KNI_4.3.0/lib/linux/libKNIBase.so KNI_4.3.0/lib/linux/libKNIBase.a
  KNI_4.3.0/lib/linux/libKNI_InvKin.so KNI_4.3.0/lib/linux/libKNI_InvKin.a
  KNI_4.3.0/lib/linux/libKNI_LM.so KNI_4.3.0/lib/linux/libKNI_LM.a
#   ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
#   RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)


## Mark cpp header files for installation
install(DIRECTORY KNI_4.3.0/include 
   #include/${PROJECT_NAME}/
   DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
   FILES_MATCHING PATTERN "*.h"
)


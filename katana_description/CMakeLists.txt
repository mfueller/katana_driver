cmake_minimum_required(VERSION 2.8.3)
project(katana_description)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS roscpp rospy sensor_msgs)

## System dependencies are found with CMake's conventions
# find_package(Boost REQUIRED COMPONENTS system)


## Uncomment this if the package has a setup.py. This macro ensures
## modules and global scripts declared therein get installed
## See http://ros.org/doc/api/catkin/html/user_guide/setup_dot_py.html
# catkin_python_setup()

#######################################
## Declare ROS messages and services ##
#######################################

## Generate messages in the 'msg' folder
# add_message_files(
#   FILES
#   Message1.msg
#   Message2.msg
# )

## Generate services in the 'srv' folder
# add_service_files(
#   FILES
#   Service1.srv
#   Service2.srv
# )

## Generate added messages and services with any dependencies listed here
# generate_messages(
#   DEPENDENCIES
#   sensor_msgs
# )

###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## INCLUDE_DIRS: uncomment this if you package contains header files
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES package_example
#  CATKIN_DEPENDS roscpp rospy sensor_msgs
#  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
# include_directories(include)
include_directories(
  ${catkin_INCLUDE_DIRS}
)

## Declare a cpp library
# add_library(package_example
#   src/${PROJECT_NAME}/package_example.cpp
# )

## Declare a cpp executable
# add_executable(package_example_node src/package_example_node.cpp)

## Add cmake target dependencies of the executable/library
## as an example, message headers may need to be generated before nodes
# add_dependencies(package_example_node package_example_generate_messages_cpp)

## Specify libraries to link a library or executable target against
# target_link_libraries(package_example_node
#   ${catkin_LIBRARIES}
# )

#############
## Install ##
#############

# all install targets should use catkin DESTINATION variables
# See http://ros.org/doc/api/catkin/html/adv_user_guide/variables.html

## Mark executable scripts (Python etc.) for installation
## in contrast to setup.py, you can choose the destination
# install(PROGRAMS
#   scripts/my_python_script
#   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

## Mark executables and/or libraries for installation
# install(TARGETS package_example package_example_node
#   ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#   LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#   RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

## Mark cpp header files for installation
# install(DIRECTORY include/${PROJECT_NAME}/
#   DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
#   FILES_MATCHING PATTERN "*.h"
#   PATTERN ".svn" EXCLUDE
# )

## Mark other files for installation (e.g. launch and bag files, etc.)
# install(FILES
#   # myfile1
#   # myfile2
#   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
# )

#############
## Testing ##
#############

## Add gtest based cpp test target and link libraries
# catkin_add_gtest(${PROJECT_NAME}-test test/test_package_example.cpp)
# if(TARGET ${PROJECT_NAME}-test)
#   target_link_libraries(${PROJECT_NAME}-test ${PROJECT_NAME})
# endif()

## Add folders to be run by python nosetests
# catkin_add_nosetests(test)




# iterate through all the stl files to:
#  1. convert to *.iv files
#  2. generate convex decomposed .stl
file(GLOB katana_stl_files ${CMAKE_CURRENT_SOURCE_DIR}/meshes/*/*.stl)
set(katana_gen_files "")

# foreach(it ${katana_stl_files})
#   get_filename_component(basepath ${it} PATH)
#   get_filename_component(basename ${it} NAME_WE)

#   IF ( ${basename} MATCHES "_convex" )

#     message("ignoring stale .._convex.stl file:",${basename})

#   ELSE ( ${basename} MATCHES "_convex" )

#     # create subdirectory convex
#     add_custom_command(
#       OUTPUT ${basepath}/convex
#       # CMake 2.4 doesn't offer the make_directory command.
#       #COMMAND ${CMAKE_COMMAND} -E make_directory
#       COMMAND mkdir -p
#       ARGS ${basepath}/convex)

#     #    # create subdirectory iv
#     #    add_custom_command(
#     #      OUTPUT ${basepath}/iv
#     #      # CMake 2.4 doesn't offer the make_directory command.
#     #      #COMMAND ${CMAKE_COMMAND} -E make_directory
#     #      COMMAND mkdir -p
#     #      ARGS ${basepath}/iv)
  
#     # copy *.stl files to *.stlb so that ivcon recognizes them as binary stl files
#     add_custom_command(
#       OUTPUT ${it}b
#       COMMAND ${CMAKE_COMMAND}
#       ARGS -E copy_if_different ${it} ${it}b
#       DEPENDS )

#     set(katana_gen_files ${katana_gen_files} ${it}b)

#     #create obj files for convex decomposition from stl files
#     add_custom_command(
#       OUTPUT ${basepath}/convex/${basename}.obj
#       COMMAND ivcon
#       ARGS ${it}b ${basepath}/convex/${basename}.obj
#       DEPENDS ${it} ${it}b ${basepath}/convex)

#     set(katana_gen_files ${katana_gen_files} ${basepath}/convex/${basename}.obj)

#     #convex decompose object files
#     add_custom_command(
#       OUTPUT ${basepath}/convex/${basename}_convex.obj
#       COMMAND convex_decomposition
#       ARGS ${basepath}/convex/${basename}.obj -v12 -p10
#       DEPENDS ${basepath}/convex/${basename}.obj ${basepath}/convex)

#     set(katana_gen_files ${katana_gen_files} ${basepath}/convex/${basename}_convex.obj)

#     #convert obj files back to stlb, put in directory named convex
#     add_custom_command(
#       OUTPUT ${basepath}/convex/${basename}_convex.stlb
#       COMMAND ivcon
#       ARGS ${basepath}/convex/${basename}_convex.obj ${basepath}/convex/${basename}_convex.stlb
#       DEPENDS ${it} ${basepath}/convex ${basepath}/convex/${basename}_convex.obj)

#     # copy *.stlb files to *.stl so that Gazebo doesn't complain about "Invalid mesh filename extension"
#     add_custom_command(
#       OUTPUT ${basepath}/convex/${basename}_convex.stl
#       COMMAND ${CMAKE_COMMAND}
#       ARGS -E copy_if_different ${basepath}/convex/${basename}_convex.stlb ${basepath}/convex/${basename}_convex.stl
#       DEPENDS ${basepath}/convex/${basename}_convex.stlb)

#     set(katana_gen_files ${katana_gen_files} ${basepath}/convex/${basename}_convex.stl)

#     #    #convert obj files back to stla, put in directory named convex
#     #    add_custom_command(
#     #      OUTPUT ${basepath}/convex/${basename}_convex.stla
#     #      COMMAND ivcon
#     #      ARGS ${basepath}/convex/${basename}_convex.obj ${basepath}/convex/${basename}_convex.stla
#     #      DEPENDS ${it} ${basepath}/convex ${basepath}/convex/${basename}_convex.obj)
#     #
#     #    set(katana_gen_files ${katana_gen_files} ${basepath}/convex/${basename}_convex.stla)

#     #    #create iv files
#     #    add_custom_command(
#     #      OUTPUT ${basepath}/iv/${basename}.iv
#     #      COMMAND ivcon
#     #      ARGS ${it}b ${basepath}/iv/${basename}.iv
#     #      DEPENDS ${basepath}/iv ${it} ${it}b)
#     #    add_custom_command(
#     #      OUTPUT ${basepath}/convex/${basename}_convex.iv
#     #      COMMAND ivcon
#     #      ARGS ${basepath}/convex/${basename}_convex.obj ${basepath}/convex/${basename}_convex.iv
#     #      DEPENDS ${it} ${basepath}/convex ${basepath}/convex/${basename}_convex.obj)
     
#     #    set(katana_gen_files ${katana_gen_files} ${basepath}/iv/${basename}.iv ${basepath}/convex/${basename}_convex.iv)


#   ENDIF ( ${basename} MATCHES "_convex" )

# endforeach(it)

add_custom_target(media_files_katana ALL DEPENDS ${katana_gen_files} )


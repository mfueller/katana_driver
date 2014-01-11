#! /usr/bin/env python

import roslib; 
import rospy
import actionlib

from katana_msgs.msg import *
from control_msgs.msg import *
from trajectory_msgs.msg import *


if __name__ == '__main__':
    rospy.init_node('do_katana_test')
    
    
    client = actionlib.SimpleActionClient('/katana_arm_controller/joint_movement_action', JointMovementAction)
    client.wait_for_server()
 
    goal = JointMovementGoal()
    # Fill in the goal here
 
    goal.jointGoal.name = ["katana_motor1_pan_joint", "katana_motor2_lift_joint", "katana_motor3_lift_joint", "katana_motor4_lift_joint", "katana_motor5_wrist_roll_joint"]
    
   # goal.jointGoal.position = [0, 0.5, 0.5, 0.5]
    
    #goal.jointGoal.velocity = [0.1, 0.1, 0.5, 0.5]
    
    #goal.jointGoal.position = [0, 0.5, 0.5, 0.5]
    #client.send_goal(goal)
    #client.wait_for_result(rospy.Duration.from_sec(5.0))

    goal.jointGoal.position = [0, 2.2, -1.7, 0.4, 1.59]
    goal.jointGoal.velocity = [0.1, 0.1, 0.1, 0.1]
    client.send_goal(goal)
    client.wait_for_result(rospy.Duration.from_sec(15.0))


    goal.jointGoal.position = [0, 0.6, -0.2, 0.2, 1.59]
    client.send_goal(goal)
    client.wait_for_result(rospy.Duration.from_sec(5.0))
    
#     client = actionlib.SimpleActionClient('katana_arm_controller/joint_trajectory_action', JointTrajectoryAction)
#     print "Wait for server"
#     
#     client.wait_for_server()
#     
#     print "Found Server"
#     
#     
#  
#   
#     msg = JointTrajectoryGoal()
#     
#     trj = JointTrajectory()
#     msg.trajectory = trj
#     
#     
#     trj.joint_names = ["katana_motor1_pan_joint", "katana_motor2_lift_joint", "katana_motor3_lift_joint", "katana_motor4_lift_joint", "katana_motor5_wrist_roll_joint"]
# #     trajectory_msgs/JointTrajectoryPoint[] points
# #       float64[] positions
# #       float64[] velocities
# #       float64[] accelerations
#     
#     p1 = JointTrajectoryPoint()
#     p1.positions = [0.1, 0.5, -2.15, -1.971949, -2.956179]
#     p1.time_from_start.nsecs = 0
#     trj.points.append(p1)
#     
#     p2 = JointTrajectoryPoint()
#     p2.positions = [0.5, 1.5, -2.15, -1.971949, -2.956179]
#     p2.time_from_start.secs = 5
#     trj.points.append(p2)
#         
#     client.send_goal(msg)
#     
#     client.wait_for_result(rospy.Duration.from_sec(5.0))
#     
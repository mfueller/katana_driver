rostopic pub -1 /katana_arm_controller/velocity_command  brics_actuator/JointVelocities '{velocities: [
{joint_uri: katana_motor1_pan_joint, unit: rad, value: 0.05},
{joint_uri: katana_motor2_lift_joint, unit: rad, value: 0.05},
{joint_uri: katana_motor3_lift_joint, unit: rad, value: 0.1},
{joint_uri: katana_motor4_lift_joint, unit: rad, value: 0.05},

]}'

from robot_control_class import RobotControl 
robotcontrol = RobotControl()
a = robotcontrol.get_laser_full()
maxim = 0

for value in a:
    
    print(value)


from robot_control_class import RobotControl 
robotcontrol = RobotControl()
import time

def get_laser_values(a,b,c):
    r1 = robotcontrol.get_laser_summit(a)
    r2 = robotcontrol.get_laser_summit(b)
    r3 = robotcontrol.get_laser_summit(c)

    return [r1,r2,r3]

d = get_laser_values(0, 500, 1000)


print ("Reading 1: ", d[0])
print ("Reading 1: ", d[1])
print ("hello", d[2])

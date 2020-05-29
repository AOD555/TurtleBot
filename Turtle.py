from robot_control_class import RobotControl
import time
z = 1
robotcontrol = RobotControl()


class MoveTurtle:
    def __init__(self,motion,clockwise, speed, time):
        self.robotcontrol = RobotControl()
        self.motion = motion
        self.clockwise = clockwise
        self.speed = speed
        self.time = time
        #self.laser = laser

    def move_straight(self):
        self.robotcontrol.move_straight_time(self.motion, self.speed, self.time)

    def turn(self):
        self.robotcontrol.turn(self.clockwise, self.speed, self.time)




# class info:
#     def __init__(self):

#     def laser(self):
#         self.robotcontrol.get_front_laser(360)
#test1 = MoveTurtle('','clockwise',0.3,4)
#test1.turn()
# Get distance then turn
i = 0
while z == 1:
    a = robotcontrol.get_front_laser()
    b = robotcontrol.get_laser(700)
    c = robotcontrol.get_laser(0)
    print(a)
    mr2 = MoveTurtle ('forward','',0.35,2)
    mr2.move_straight()
    if a < 2:
        z = 2
    while z == 2:
    
        a = robotcontrol.get_front_laser()
        b = robotcontrol.get_laser(0)
        c = robotcontrol.get_laser(700)
        print(b)
        print(c)
        if b > c:
            mr3 = MoveTurtle("","clockwise",0.3,4)
            mr3.turn()
            z = 1
        
            #z = 1
        elif b < c:
            mr4 = MoveTurtle("","counter",0.3,4)
            mr4.turn()
            z = 1
        


print(a)
# while a > 1:
#     mr2 = MoveTurtle ('forward','',0.3,1)
#     mr2.move_straight()
#     print(a)
    

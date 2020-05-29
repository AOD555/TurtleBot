from robot_control_class import RobotControl
import time

class MoveRobot:
    def __init__(self,motion,clockwise, speed, time):
        self.robotcontrol = RobotControl()
        self.motion = motion
        self.clockwise = clockwise
        self.speed = speed
        self.time = time
        self.time_turn = 7.0 # takes 7 seconds to turn 90 degress

    def do_square(self):
        i = 0

        while (i < 4):
            self.move_straight()
            self.turn()
            i+=1
    def move_straight(self):
        self.robotcontrol.move_straight_time(self.motion,self.speed,self.time)
        # The line above needs the be send the parameters to see what motion, speed dand time

    def turn(self):
        self.robotcontrol.turn(self.clockwise,self.speed,self.time_turn)
        #Needs to send parameters to this also
mr2 = MoveRobot('forward','',0.3,10)
mr2.move_straight()
#mr1 = MoveRobot('forward','clockwise', 0.3,4)
#mr1.do_square()


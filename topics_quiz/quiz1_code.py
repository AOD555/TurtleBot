#! /usr/bin/env python
 
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Int32
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
import time


def callback(msg):
    if msg.ranges[360] > 1.0:
        move.linear.x = 0.5
        move.angular.z = 0.5
        print msg.ranges[360]
        pub = rospy.Publisher('topics_quiz_node', String, queue_size=10)


    if msg.ranges[360] < 1.0:
        move.linear.x = 0.5
        move.angular.z = -0.5
        print msg.ranges[360]
 
    
    
 
rospy.init_node('topics_quiz_node')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1) #Create a Publisher that will publish in the /age_info topic
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)

# rospy.spin()



move = Twist()


while not rospy.is_shutdown(): 
  pub.publish(move)
  time.sleep(2)


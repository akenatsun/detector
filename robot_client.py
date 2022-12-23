#!/usr/bin/env python

from _future_ import print_function
import rospy
from your_package.srv import Location , Nav
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib_msgs.msg import *
from std_msgs.msg import Float32

def go_to_location_client(self,depth):
    rospy.init_node('go_to_location')
    rospy.wait_for_service('robot_following')
    rate = rospy.Rate(1000000)
    robot_following = rospy.ServiceProxy('robot_following', Location)
    print("input location")
    resp1 = robot_following(self.depth-10)
    print(resp1)


if _name_ == '_main_':
    go_to_location_client(1)

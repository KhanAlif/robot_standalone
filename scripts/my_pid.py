#!/usr/bin/env python3

import rospy
import roslib

from std_msgs.msg import Int16,Int64
from std_msgs.msg import Float32
from numpy import array



class PidVelocity():

    def __init__(self):
        rospy.init_node("pid_velocity")
        self.nodename = rospy.get_name()
        rospy.loginfo("%s started" % self.nodename)
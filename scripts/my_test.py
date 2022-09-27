#!/usr/bin/env python3

import rospy

rospy.init_node("mother_chod")

while not rospy.is_shutdown():
    seconds = rospy.get_time()
    rospy.loginfo("Current time %f", seconds)

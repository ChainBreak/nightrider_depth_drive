#!/usr/bin/env python

# IMPORT CLASSES
import cv2
import math
import rospy
import numpy as np
from cv_bridge import CvBridge

# IMPORT MESSAGE TYPES
from ackermann_msgs.msg import AckermannDriveStamped
from sensor_msgs.msg import Image


class DepthDriver():
    def __init__(self):

        self.depth_subscriber = rospy.Subscribe("camera/depth/image_rect_raw", Image, self.callback_depth_image)

        self.bridge = CvBridge()

    def callback_depth_image(self,data):
        rospy.loginfo("Depth Image Received")
        img_depth = self.bridge.imgmsg_to_cv2(data)

        cv2.imshow("depth",img_depth)

if __name__ == "__main__":
    rospy.init_node("depth_drive")

    while not rospy.is_shutdown():
        cv2.waitKey(20)
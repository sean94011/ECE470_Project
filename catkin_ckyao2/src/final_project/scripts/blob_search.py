#!/usr/bin/env python

import cv2
import numpy as np
from numpy.linalg import norm
import math

# ========================= Student's code starts here =========================

# Params for camera calibration
theta = -0.016
beta = 743.8
tx = 0.29
ty = 0.105

# Function that converts image coord to world coord
# Note: input x corresponds to columns in the image, input y is rows in the image
def IMG2W(x,y):
    beta = 743.8
    theta = -0.016
    R = rot_mat(theta).T
    x_c = (y-240)/beta
    y_c = (x-320)/beta
    c_coor = np.array([x_c, y_c, 0]).T
    T_coor = np.array([tx,ty,0]).T
    world_coor = np.matmul(R,c_coor)+T_coor
    return [world_coor[0], world_coor[1]]


# ========================= Student's code ends here ===========================

def blob_search(image_raw, color):

    # Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()

    # ========================= Student's code starts here =========================


    # Filter by Color
    params.filterByColor = False

    # Filter by Area.
    params.filterByArea = True
    params.minArea = 400
    params.maxArea = 800

    # Filter by Circularity
    params.filterByCircularity = False
    #params.minCircularity = 0.5
    #params.maxCircularity = 1.1

    # Filter by Inerita
    params.filterByInertia = False

    # Filter by Convexity
    params.filterByConvexity = False

    # ========================= Student's code ends here ===========================

    # Create a detector with the parameters
    detector = cv2.SimpleBlobDetector_create(params)

    # Convert the image into the HSV color space
    hsv_image = cv2.cvtColor(image_raw, cv2.COLOR_BGR2HSV)

    # ========================= Student's code starts here =========================

    if color is "green":
        lower = (60,50,50)
        upper = (80,255,255)   # green upper
    """if color is "purple":
        lower = (125,20,20)
        upper = (145,250,250)   # purple upper"""
    """
    else:
        lower = (5,50,50)
        upper = (15,255,255)   # orange upper
    """

    # Define a mask using the lower and upper bounds of the target color
    mask_image = cv2.inRange(hsv_image, lower, upper)

    # ========================= Student's code ends here ===========================

    keypoints = detector.detect(mask_image)

    # Find blob centers in the image coordinates
    blob_image_center = []
    num_blobs = len(keypoints)
    for i in range(num_blobs):
        blob_image_center.append((keypoints[i].pt[0],keypoints[i].pt[1]))

    # Draw the keypoints on the detected block
    im_with_keypoints = cv2.drawKeypoints(image_raw, keypoints, None, color=(230,115,25))

    xw_yw = []

    if(num_blobs == 0):
        print("No block found!")
    else:
        # Convert image coordinates to global world coordinate using IM2W() function
        for i in range(num_blobs):
            xw_yw.append(IMG2W(blob_image_center[i][0], blob_image_center[i][1]))
    
    cv2.namedWindow("Camera View")
    cv2.imshow("Camera View", image_raw)
    cv2.namedWindow("Mask View")
    cv2.imshow("Mask View", mask_image)

    cv2.namedWindow("Keypoint View")
    cv2.imshow("Keypoint View", im_with_keypoints)

    cv2.waitKey(2)

    return xw_yw

def rot_mat(theta):
    return np.array([
        [np.cos(theta), -1*np.sin(theta), 0],
        [np.sin(theta), np.cos(theta),    0],
        [0, 0, 1]
    ]).T
import cv2
import numpy as np

def get_limits(color):
    c = np.uint8([[color]])
    hsv = cv2.cvtColor(c,cv2.COLOR_BGR2HSV)

    hue = hsv[0][0][0]#hue value of the hsv image

    if hue>=165:
        lower_limit = np.array([hue-10,100,100])
        upper_limit = np.array([180,255,255])

    elif hue<=15:
        lower_limit = np.array([hue,100,100])
        upper_limit = np.array([hue+10,255,255])
    else:
        lower_limit = np.array([hue-10,100,100])
        upper_limit = np.array([hue+10,255,255])

    return lower_limit,upper_limit  
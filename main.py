import cv2
import numpy as np
from PIL import Image
from utils import get_limits

yellow = [0,255,255]
cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    img_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lower_limit,upper_limit = get_limits(color = yellow)
    mask = cv2.inRange(img_hsv,lower_limit,upper_limit)
    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()
    # print(bbox)
    if bbox is not None:
        x1,y1,x2,y2 = bbox
        frame = cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),4)
    cv2.imshow("frame",frame)
    if cv2.waitKey(40) & 0XFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()    

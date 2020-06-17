import cv2
import numpy as np

device = cv2.VideoCapture(0)

while True:
    ret,frame = device.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    l_range = np.array([110,50,50])
    h_range = np.array([130,255,255])
    mask = cv2.inRange(hsv, l_range, h_range)
    cv2.imshow('show',mask)
    cv2.imshow('show1',frame)

    if cv2.waitKey(13) == 13:
        break

device.release()
cv2.destroyAllWindows()


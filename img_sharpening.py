import cv2
import numpy as np

img = cv2.imread('plane.jpg')
cv2.imshow('Frame',img)

cv2.waitKey(0)

#summation of al value = 1
kernel_sharp=np.array([[-1,-1,-1],
[-1,9,-1],
[-1,-1,-1]])

sharpened = cv2.filter2D(img,-1,kernel_sharp)

cv2.imshow('frame',sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()

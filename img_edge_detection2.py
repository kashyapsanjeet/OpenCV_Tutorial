import cv2
import numpy as np

img =cv2.imread('plane.jpg',0)
cv2.imshow('frame',img)
cv2.waitKey(0)

#laplacian edge detection
laplacian = cv2.Laplacian(img,cv2.CV_64F)
cv2.imshow('edge',laplacian)
cv2.waitKey(0)

#canny edge detection
canny = cv2.Canny(img,20,500)
cv2.imshow('Canny Edge',canny)
cv2.waitKey(0)


cv2.destroyAllWindows()
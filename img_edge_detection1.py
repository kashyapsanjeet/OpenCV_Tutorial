import cv2
import numpy as np

img =cv2.imread('plane.jpg',0)
cv2.imshow('frame',img)
cv2.waitKey(0)

height,width = img.shape[:2]

#extract slop edges
sobel_x = cv2.Sobel(img,cv2.CV_64F,1 , 0 , ksize=5)
sobel_y = cv2.Sobel(img,cv2.CV_64F,0 , 1 , ksize=5)

cv2.imshow('sobel_X_img',sobel_x)
cv2.waitKey(0)

cv2.imshow('sobel_y_img',sobel_y)
cv2.waitKey(0)

sobel_or=cv2.bitwise_or(sobel_x,sobel_y)
cv2.imshow('sobel_or',sobel_or)
cv2.waitKey(0)
cv2.destroyAllWindows()
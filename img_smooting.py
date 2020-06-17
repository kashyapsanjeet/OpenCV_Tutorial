import cv2
import numpy as np

img =cv2.imread('plane.jpg')
cv2.imshow('frame',img)
cv2.waitKey(0)

#Box filter
blur = cv2.blur(img,(3,3))
cv2.imshow('Blur Image',blur)
cv2.waitKey(0)

#gaussian blur
g_blur = cv2.GaussianBlur(img,(7,7),0)
cv2.imshow('g_blur',g_blur)
cv2.waitKey(0)

#median blur
m_blur = cv2.medianBlur(img,5)
cv2.imshow('m_blur',m_blur)
cv2.waitKey(0)

#median blur
b_blur = cv2.bilateralFilter(img,9,75,75)
cv2.imshow('b_blur',b_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
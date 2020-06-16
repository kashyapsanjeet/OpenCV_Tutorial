#Scaling resizing and interpolation

import cv2

img=cv2.imread('plane.jpg')

cv2.imshow('frame',img)

img_scaled = cv2.resize(img,None,fx=0.50,fy=0.50)
cv2.imshow('frame2_resized_linear_interpolation',img_scaled)

img_scaled2 = cv2.resize(img,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_CUBIC)
cv2.imshow('frame2_resized_cubic_interpolation',img_scaled2)

img_scaled3 = cv2.resize(img,(400,400),interpolation=cv2.INTER_AREA)
cv2.imshow('frame2_resized_skewed_size',img_scaled3)

cv2.waitKey(0)

cv2.destroyAllWindows()
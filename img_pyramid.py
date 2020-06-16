# image resize using image pyramid

import cv2

img=cv2.imread('plane.jpg')

cv2.imshow('frame',img)

cv2.waitKey(0)

smaller = cv2.pyrDown(img)  #image half
cv2.imshow('frame2',smaller)

cv2.waitKey(0)

larger = cv2.pyrUp(img) #image double
cv2.imshow('fram3',larger)


cv2.waitKey(0)
cv2.destroyAllWindows()
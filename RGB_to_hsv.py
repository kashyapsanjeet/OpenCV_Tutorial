#Hue : 0-180 , Saturation : 0-255 , Value : 0-255
import cv2

img=cv2.imread('plane.jpg')

img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow('frame',img_hsv)

cv2.imshow('Hue Channel',img_hsv[:,:,0])
cv2.imshow('saturation Channel',img_hsv[:,:,1])
cv2.imshow('value Channel',img_hsv[:,:,2])

cv2.waitKey(0)

cv2.destroyAllWindows()
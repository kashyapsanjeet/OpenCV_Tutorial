import cv2

img=cv2.imread('plane.jpg',0)

cv2.imshow('grey',img)

cv2.waitKey(0)

ret,img2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow('frame',img2)

cv2.waitKey(0)

cv2.destroyAllWindows()
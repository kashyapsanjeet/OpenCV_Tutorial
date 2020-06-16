import cv2

img=cv2.imread('plane.jpg',0)

cv2.imshow('gray_scale',img)

cv2.waitKey(0)

cv2.destroyAllWindows()
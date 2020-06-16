import cv2

img=cv2.imread('plane.jpg')

cv2.imshow('frame',img)

cv2.waitKey(0)

grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('Gray_scale',grey)

cv2.waitKey(0)

cv2.destroyAllWindows()
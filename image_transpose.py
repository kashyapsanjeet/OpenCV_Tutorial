import cv2

img=cv2.imread('1.jfif')

rotated_img=cv2.transpose(img)

cv2.imshow('frame',rotated_img)
cv2.imshow('frame2',img)

cv2.waitKey(0)

cv2.destroyAllWindows()
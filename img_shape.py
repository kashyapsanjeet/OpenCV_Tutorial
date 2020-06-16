import cv2

img=cv2.imread('plane.jpg')

cv2.imshow('frame',img)
print(img.shape)

cv2.waitKey(0)

cv2.destroyAllWindows()
import cv2
import numpy as np

img=cv2.imread('plane.jpg')

height,width=img.shape[:2]
cv2.imshow('frame',img)
print(height,width)
cv2.waitKey(0)

quarter_height,quarter_width=height/4,width/4
print(quarter_height,quarter_width)

T=np.float32([[1,0,quarter_width],[0,1,quarter_height]])
print(T)

img_translation = cv2.warpAffine(img,T,(width,height))
cv2.imshow('frame2',img_translation)
cv2.waitKey(0)

cv2.destroyAllWindows()
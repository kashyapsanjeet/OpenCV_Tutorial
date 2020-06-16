import cv2
import numpy as np

img=cv2.imread('plane.jpg')

cv2.imshow('frame',img)

height,width=img.shape[:2]

cv2.waitKey(0)

#starting pixel coordinates
start_row,start_col = int(height * .25),int(width*.25)

#ending pixel coordiinates
end_row, end_col = int(height*.75),int(width*.75)

cropped = img[start_row:end_row,start_col:end_col]

cv2.imshow('frame2',cropped)


cv2.waitKey(0)

cv2.destroyAllWindows()
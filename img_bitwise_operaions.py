import cv2
import numpy as np

square = np.zeros((300,300) , np.uint8)

cv2.rectangle(square , (50,50) , (250,250) , 255 , -1)
cv2.imshow('square',square)

ellipse = np.zeros((300,300) , np.uint8)
cv2.ellipse(ellipse,(150,150),(150,150),30,0,180,255,-1)
cv2.imshow('Ellipse',ellipse)

cv2.waitKey(0)
And = cv2.bitwise_and(square,ellipse)
cv2.imshow('AND',And)

OR = cv2.bitwise_or(square,ellipse)
cv2.imshow('OR',OR)

NOT = cv2.bitwise_not(ellipse)
cv2.imshow('NOT',NOT)

xor = cv2.bitwise_xor(ellipse,square)
cv2.imshow('XOR',xor)

cv2.waitKey(0)

cv2.destroyAllWindows()
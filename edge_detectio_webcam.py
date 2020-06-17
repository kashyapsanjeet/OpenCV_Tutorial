import cv2
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    canny = cv2.Canny(frame,20,360)
    cv2.imshow('Canny Edge',canny)

    if cv2.waitKey(1)==13:
        break
cap.release()
cv2.destroyAllWindows()
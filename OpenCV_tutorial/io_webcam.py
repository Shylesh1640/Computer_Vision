import os
import cv2

#reading from webcam
webcam = cv2.VideoCapture(0)

while True:
    ret, frame = webcam.read()
    if not ret:
        break
    cv2.imshow('webcam', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
webcam.release()
cv2.destroyAllWindows()
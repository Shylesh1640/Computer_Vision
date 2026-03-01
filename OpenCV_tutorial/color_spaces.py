import os
import cv2

img = cv2.imread(os.path.join('.','OpenCV_tutorial','shylesh.jpg'))

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#cv2.imshow('original', img)
cv2.imshow('rgb', img_rgb)  
cv2.waitKey(10000)
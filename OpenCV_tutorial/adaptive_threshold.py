import os 
import cv2

img = cv2.imread(os.path.join('.','OpenCV_tutorial', 'handwriting.jpg'))
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
threash = cv2.adaptiveThreshold(img_grey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)

cv2.imshow('Original Image', img)
cv2.imshow('Grey Image', img_grey)
cv2.imshow('Adaptive Threshold Image', threash)
cv2.waitKey(5000)
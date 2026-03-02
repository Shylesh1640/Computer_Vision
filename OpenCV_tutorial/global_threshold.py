import os 
import cv2

img = cv2.imread(os.path.join('.', 'OpenCV_tutorial', 'bear.jpg'))
img_resize =  cv2.resize(img, (450,400))
img_grey = cv2.cvtColor(img_resize, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_grey, 80, 255, cv2.THRESH_BINARY)
blurred = cv2.blur(thresh, (7,7))

#cv2.imshow('Original Image', img)
# cv2.imshow('Resized Image', img_resize)
# cv2.imshow('Grey Image', img_grey)
# cv2.imshow('Threshold Image', thresh)
cv2.imshow('Blurred Image', blurred)
cv2.waitKey(5000)
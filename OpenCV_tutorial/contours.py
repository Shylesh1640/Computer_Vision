import os
import cv2

img = cv2.imread(os.path.join('.','OpenCV_tutorial','birds.jpg'))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if cv2.contourArea(cnt) > 200:
        cv2/drawCounters(img, [cnt], -1, (0,255,0), 3)
    print(cv2.contourArea(cnt))

#cv2.imshow('Original Image', img)
#cv2.imshow('Threshold Image', thresh)
cv2.imshow('Contours Image', img)
cv2.waitKey(3000)
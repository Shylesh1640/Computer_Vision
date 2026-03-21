import os
import cv2

img = cv2.imread(os.path.join('.','OpenCV_tutorial','cow.jpg'))

k_size = 7
#clasical blur
blurred1 = cv2.blur(img, (k_size, k_size))
#gaussian blur
blurred2 = cv2.GaussianBlur(img, (k_size, k_size), 5)
#median blur
blurred3 = cv2.medianBlur(img, k_size)

cv2.imshow('Original Image', img)
cv2.imshow('Classical Blurred Image', blurred1)
cv2.imshow('Gaussian Blurred Image', blurred2)
cv2.imshow('Median Blurred Image', blurred3)
cv2.waitKey(0)


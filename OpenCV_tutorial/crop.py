#crop an image

import os
import cv2

img = cv2.imread(os.path.join('.','OpenCV_tutorial','rain.jpg'))
print(img.shape)

cropped_img = img[200:300, 500:800]
print(cropped_img.shape)

cv2.imshow('original', img)
# cv2.waitKey(3000)
cv2.imshow('cropped', cropped_img)
cv2.waitKey(9000)
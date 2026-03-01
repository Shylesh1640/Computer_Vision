#resizing an image

import os
import cv2

img = cv2.imread(os.path.join('.','OpenCV_tutorial','rain.jpg'))
img_resized = cv2.resize(img, (350, 400))

print(img.shape)
print(img_resized.shape)

# cv2.imshow('original', img)
# cv2.waitKey(3000)
cv2.imshow('resized', img_resized)
cv2.waitKey(9000)

#resizing the image


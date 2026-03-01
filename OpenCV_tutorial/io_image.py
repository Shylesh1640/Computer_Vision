import os

import cv2

# reading the image 
image_path = os.path.join(os.getcwd(), 'OpenCV_tutorial', 'image.jpg')

img = cv2.imread(image_path)

#writing the image 
cv2.imwrite(os.path.join('.', 'OpenCV_tutorial','rain.jpg'), img)

cv2.imshow('image', img)
cv2.waitKey(3000)
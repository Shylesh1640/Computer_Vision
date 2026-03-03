import os
import cv2
import numpy as np


img_resized = cv2.imread(os.path.join("OpenCV_tutorial", "basket_ball_player.jpg"))
img = cv2.resize(img_resized, (350, 400))

edges = cv2.Canny(img, 100, 200)

img_dilate = cv2.dilate(edges, np.ones((2,2),dtype=np.uint8), iterations=1)

img_erode = cv2.erode(img_dilate, np.ones((2,2),dtype=np.uint8), iterations=1)

cv2.imshow("Original Image", img)
cv2.imshow("Edges", edges)
cv2.imshow("Dilated Edges", img_dilate)
cv2.imshow("Eroded Edges", img_erode)
cv2.waitKey(4000)
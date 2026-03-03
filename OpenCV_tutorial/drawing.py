import os
import cv2

img = cv2.imread(os.path.join('.','OpenCV_tutorial','whiteboard.jpg'))

#line
cv2.line(img,(0,0),(150,100),(255,0,0),2)
cv2.line(img,(150,100),(200,150),(255,0,0),2)
cv2.line(img,(200,150),(0,0),(255,0,0),2)
#rectangle
cv2.rectangle(img,(10,10),(100,100),(0,255,0),3)
#circle
cv2.circle(img,(200,200),180,(0,0,255),20)
#text
cv2.putText(img,'SHYLESH S',(300,300),cv2.FONT_HERSHEY_SIMPLEX,1,(100,100,0),2)

cv2.imshow('image',img)
cv2.waitKey(4000)
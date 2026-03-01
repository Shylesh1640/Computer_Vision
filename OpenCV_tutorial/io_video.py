import os

import cv2

#reading the video
video_path = os.path.join('.', 'OpenCV_tutorial', 'video.mp4')

video = cv2.VideoCapture(video_path)

#visualize the video
ret = True
while ret:
    ret, frame = video.read()
    if ret:
        cv2.imshow('video', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
video.release()
cv2.destroyAllWindows()
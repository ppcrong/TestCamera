# -*- coding: utf-8 -*-
import cv2

cam = cv2.VideoCapture(0)

while True:
    # https://tinyurl.com/y7yxj7p2
    # ret, img = cam.read()
    # vis = img.copy()
    # cv2.imshow('Camera', vis)

    # https://zhuanlan.zhihu.com/p/95624918
    # Capture frame-by-frame
    ret, frame = cam.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
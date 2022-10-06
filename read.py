# Importing OpenCV library

import cv2 as cv
#Reading images

# img1 = cv.imread('pics/cat1.jpeg')
# img2 = cv.imread('pics/dog2.jpeg')

# cv.imshow('dog', img2)

#Reading videos

capture_vid = cv.VideoCapture('videos/Cute Cat - 3092.mp4')

while True:
    isTrue, frame = capture_vid.read()
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break




capture.release()
cv.destroyAllWindows()



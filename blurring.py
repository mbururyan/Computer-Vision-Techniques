import cv2 as cv

image = cv.imread('Other Pics/park.jpeg')

cv.imshow('park', image)

# Blur

blurred = cv.GaussianBlur(image, (5,5), cv.BORDER_DEFAULT)

cv.imshow('blurred park', blurred)

cv.waitKey(0)
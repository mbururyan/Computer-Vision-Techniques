import cv2 as cv

image = cv.imread('Other Pics/park.jpeg')

cv.imshow('park', image)

#Cascade the edges

cascade1 = cv.Canny(image, 125, 175)

cv.imshow('edges', cascade1)

#Amount of edges can be reduced by applying blur to the image first

cv.waitKey(0)


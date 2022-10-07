import cv2 as cv
import numpy as np


image = cv.imread('Other Pics/cats 2.jpeg')

cv.imshow('OG cats', image)

#Grayscale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# # Blur abit
# blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

#Edges
canny = cv.Canny(gray, 125, 175)
cv.imshow('Edges', canny)

# Blank image for contour viz
blank = np.zeros(image.shape, dtype='uint8')
cv.imshow('blank', blank)

# No of contours
contours, hierachies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found !')

# Visualize the contours
cv.drawContours(blank, contours, -1, (0,255,0), 1)
cv.imshow('contours', blank)


cv.waitKey(0)
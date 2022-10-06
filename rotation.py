import cv2 as cv
import numpy as np

image = cv.imread('Other Pics/cat.jpeg')

cv.imshow('OG', image)

# Rotated

def rotate(img, angle, rotPoint  = None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimension = (width, height)

    return cv.warpAffine(img, rotMat, dimension)

rotated = rotate(image, 90)
cv.imshow('rotated', rotated)

# Rotating the rotated image

rotated_square = rotate(rotated, 90)
cv.imshow('rotated squared', rotated_square)




# Resizing rotated image

resized = cv.resize(image, (500, 500), interpolation=cv.INTER_CUBIC)

cv.imshow('resized', resized)

cv.waitKey(0)




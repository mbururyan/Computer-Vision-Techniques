import cv2 as cv
import numpy as np

# Image transformations

image = cv.imread('/Volumes/Rayo HDD/Computer Vision/FreeCodeCamp YT/Img Manipulation/Other Pics/cat.jpeg')

cv.imshow('OG', image)

# Translation

def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated_image = translate(image, 100, 100)
cv.imshow('translated', translated_image)

translated_image2 = translate(image, -100, -100)
cv.imshow('translated 2', translated_image2)

cv.waitKey(0)
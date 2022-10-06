import cv2 as cv

# Converting to greyscale

image = cv.imread('pics/dog2.jpeg')


gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('grey', image)



cv.waitKey(0)
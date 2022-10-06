import cv2 as cv

image = cv.imread('/Volumes/Rayo HDD/Computer Vision/FreeCodeCamp YT/Img Manipulation/Other Pics/park.jpeg')

cv.imshow('OG', image)

# #cropped
# cropped = image[50:200, 200:40]
# cv.imshow('cropped', cropped)

cv.waitKey(0)


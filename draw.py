import cv2 as cv
import numpy as np

# Import cat pic

cat1 = cv.imread('pics/cat5.jpeg')

# Increase the size of the image

# def rescaleFrame(frame, scale = 2.0):
#     width = int(frame.shape[1] * scale)
#     height = int(frame.shape[0] * scale)

#     dimensions = (width, height)

#     return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

# #rescaled cat pic

# rescaled_cat1 = rescaleFrame(cat1)

# # cv.imshow('cat pic 1', cat1)
# cv.imshow('new cat pic', rescaled_cat1)

# Blank image to draw on

blank_pic = np.zeros((500,500, 3), dtype='uint8')

cv.imshow('blank space', blank_pic)



# Paint the image a colour

# blank_pic[:] = 0, 0, 255

# cv.imshow('red', blank_pic)



# Paint a certain portion

# blank_pic[200:300, 300:400] = 0,0, 255

# cv.imshow('portion', blank_pic)


#Rectangle 

cv.rectangle(blank_pic, (0,0), (250, 250), (0, 255, 0), thickness = 2)

cv.imshow('rectangle', blank_pic)

# Circle

cv.circle(blank_pic, (blank_pic.shape[1]//2, blank_pic.shape[0]//2), 15, (0,0, 255), thickness = 1)
cv.imshow('circle', blank_pic)

# Text

cv.putText(blank_pic, 'TEXT', (250, 300), cv.FONT_HERSHEY_TRIPLEX, 0.5, (0,255,0), 1)
cv.imshow('text', blank_pic)


cv.waitKey(0)




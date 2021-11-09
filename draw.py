
import cv2 as cv
import numpy as np

# Blank image
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# img = cv.imread('./Pictures/dog1.jpg')
# cv.imshow('Dog', img)
# 1. Paint the image a certain color
blank[:] = 0, 255, 0
# just part of the image with color
# blank[200:300, 300:300] = 0, 0, 255
cv.imshow('Green', blank)


# 2.Draw rectangle
cv.rectangle(blank, (0,0), (150, 250), (0,0,255), thickness=2)
cv.imshow('Rectangle', blank)

# 3. Draw Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=5)
cv.imshow('Circle', blank)
cv.waitKey(0)

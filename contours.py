# contours are the boundaries of an object
# contours are used to find the area of an object

import cv2 as cv
import numpy as np


img = cv.imread('./Photos/Cat_small.jpg')
cv.imshow('Original', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank_image', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur = cv.GaussianBlur(gray, (3, 3), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

# canny = cv.Canny(blur, 225, 225)
# cv.imshow('Canny Edges', canny)

ret, thresh = cv.threshold(gray, 105, 225, cv.THRESH_BINARY)
# if pixel less than thresh value, it is set to 0 else it is set to 255
cv.imshow('Thresholded Image', thresh)


contours, hierarchies = cv.findContours(
    thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found')

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours drawn image', blank)

cv.waitKey(0)

''''
Masking allows us to focus on the parts of the image that we want to keep.
'''

import cv2 as cv
from cv2 import rectangle
import numpy as np


img = cv.imread('./Photos/cats.jpg')
cv.imshow('cats', img)

# The blank size should be the same as the image size
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank image', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2+10,
                                  img.shape[0]//2 - 45), 80, 255, -1)
cv.imshow('Mask', circle)

rectangle = cv.rectangle(blank.copy(), (30, 30), (410, 410), 255, -1)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('Weird shape', weird_shape)

masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow('Masked', masked)
cv.waitKey(0)

'''
0 --> pixel is turned off
1 --> pixel is turned on
'''

import cv2 as cv
from cv2 import bitwise_or
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# Bitwise AND --> Intersecting regions
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)

# Bitwise OR --> Union regions
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise_or', bitwise_or)

# Bitwise XOR --> non-Intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('bitwise_xor', bitwise_xor)

# Bitwise NOT --> Inverse of the image
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("Bitwise_not", bitwise_not)

cv.waitKey(0)

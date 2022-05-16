'''
Color spaces are represented as an array of pixels colors.
e.g : RGB, grayscale, HSV, etc..

'''

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("./Photos/Cat_small.jpg")
cv.imshow("BGR", img)
# plt.imshow(img)
# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale", gray)

# BGR to HSV (Hue, Saturation, Value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

# BGR to Lab (Luminance, a, b)
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow("Lab", lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)
# plt.imshow(rgb)
# plt.show()

converted_grayscale = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
cv.imshow('Grayscale2', converted_grayscale)

cv.waitKey(0)

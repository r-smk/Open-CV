'''
Histograms are used to visualize the pixel intensity distribution in an image.
'''
from turtle import color
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('./Photos/Cat_small.jpg')
cv.imshow('cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Grayscale Histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])

plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')

# Color histogram
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of Pixels')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
plt.show()

cv.waitKey(0)

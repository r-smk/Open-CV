import cv2 as cv

# Reading an image
img = cv.imread('./Photos/Cat.jpg')
cv.imshow('Cat', img)


cv.waitKey(0)

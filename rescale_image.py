import cv2 as cv
from cv2 import resize


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# Reading images
img = cv.imread('./Photos/cat.jpg')
resized_image = rescaleFrame(img, 0.1)
cv.imshow('Cat', img)
cv.imshow('Rescaled Image', resized_image)

cv.waitKey(0)

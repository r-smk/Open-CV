import cv2 as cv
from cv2 import resize
import numpy as np

img = cv.imread('./Photos/Cat_small.jpg')
cv.imshow('Original', img)

# Translation


def translate(image, x, y):
    # x and y specifies the number of pixels to shift the image along x and y axis

    transMAT = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, transMAT, dimensions)


# -x --> left
# -y --> up
# +x --> right
# +y --> down
translated = translate(img, -100, -100)
cv.imshow('Translated', translated)

# Rotation


def rotate(img, angle, rotationPoint=None):
    (height, width) = img.shape[:2]

    if rotationPoint is None:
        rotationPoint = (width // 2, height // 2)

    rotationMatrix = cv.getRotationMatrix2D(rotationPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotationMatrix, dimensions)


rotated_image = rotate(img, -45)
cv.imshow('Rotated', rotated_image)

rotated_rotated = rotate(rotated_image, -45)
cv.imshow('Rotated Rotated', rotated_rotated)


# Resizing
# shrinking --> cv.INTER_AREA
# Enlarging --> cv.INTER_CUBIC(slower but better) / cv.INTER_LINEAR(faster but less accurate)
resized = cv.resize(img, (400, 1000), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)


# Flipping
# 0 --> vertical
# 1 --> horizontal
# -1 --> both vertical and horizontal
flip = cv.flip(img, -1)
cv.imshow('Flipped', flip)


# Cropping
cropped = img[200:400, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)

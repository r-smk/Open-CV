import cv2 as cv

img = cv.imread('./Photos/nature.jpg')
cv.imshow('Cat Image', img)

# # Converting to grayscale image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image', gray)

# Blur an image
# The more the kernel size, the more the blur
# kernel size should be odd
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur Image', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 225)
cv.imshow('Canny edges', canny)

# Dilating the Edges
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow('Dilated edges', dilated)

# Erdoing
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow('Eroded edges', eroded)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow('Resized image', resized)

# Cropping
cropped = img[50:250, 100:300]
cv.imshow('Cropped image', cropped)

cv.waitKey(0)

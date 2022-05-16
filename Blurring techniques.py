import cv2 as cv

img = cv.imread("./Photos/cats.jpg")
cv.imshow('Cats', img)

# Averaging
avg = cv.blur(img, (3, 3))
cv.imshow('Averaging', avg)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral Blurring(mostly used)
'''
It applies the blurring but it retains the edges.
'''
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral Blur', bilateral)

cv.waitKey(0)

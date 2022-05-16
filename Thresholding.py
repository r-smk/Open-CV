'''
Thresholding is a binarisation of an image. Converting an image into binary format.
'''
import cv2 as cv

img = cv.imread("./Photos/cats.jpg")
cv.imshow("Cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Simple Thresholding (In advanced, it won't work)
# thresh is the thresholded image,
# threshold is the same value that is passed(here 150)
threshold, thresh = cv.threshold(gray, 170, 255, cv.THRESH_BINARY)
cv.imshow("Simple Thresholded", thresh)

threshold, thresh_inv = cv.threshold(gray, 170, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simple Thresholded inverse", thresh_inv)


# Adaptive thresholding
# Blocksize --> the kernel size in which opencv uses to compute the mean value
# C --> value which is subtracted from the mean calculated to fine tune the value
adaptive_thresh = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow("Adaptive thresholding", adaptive_thresh)

adaptive_thresh = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow("Adaptive thresholding(Gaussian)", adaptive_thresh)


cv.waitKey(0)

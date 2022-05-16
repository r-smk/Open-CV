import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint the image a certain colour
# blank[200:300, 300:400] = 0, 0, 255  # BGR
# cv.imshow('Red', blank)


# 2. Draw a Rectangle
# cv.rectangle(blank, (0, 0), (250, 250), (0, 250, 0), thickness=-1)
# --> Alternatively
# cv.rectangle(blank, (0, 0),
#              (blank.shape[1]//2, blank.shape[0]//2), (0, 225, 0), thickness=cv.FILLED)
# cv.imshow('Rectangle', blank)

# 3. Draw A Circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2),
#           40, (0, 0, 255), thickness=3)
# cv.imshow('Circle', blank)

# 4. Draw a Line
# cv.line(blank, (0, 0), (250, 250), (255, 250, 255), thickness=3)
# cv.imshow('Line', blank)

# 5. Write A Text On Image
cv.putText(blank, "Hello World My name is SMK", (0, 225),
           cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 225, 0), thickness=3)
cv.imshow('Text', blank)

cv.waitKey(0)

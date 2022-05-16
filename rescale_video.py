import cv2 as cv


def changeResolution(width, height):
    # This only work for Live Videos only
    capture.set(3, width)
    capture.set(4, height)


def rescaleFrame(frame, scale=0.75):
    # This will work for
    # Images, Videos and Live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# Reading Videos
capture = cv.VideoCapture('./Videos/Dog_video3.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=0.2)

    cv.imshow('Video', frame)
    cv.imshow('Frame resized', frame_resized)

    if cv.waitKey(1) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)

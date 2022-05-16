import cv2 as cv

# Reading videos
capture = cv.VideoCapture('./Videos/Dog_video3.mp4')

while True:
    # Read frame-by-frame
    isTrue, frame = capture.read()

    cv.imshow('Video', frame)

    if cv.waitKey(0) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

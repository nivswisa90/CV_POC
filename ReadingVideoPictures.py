import cv2 as cv

# Image reading
img = cv.imread('./Pictures/dog1.jpg')

# Video reading
capture = cv.VideoCapture('./Video/dogVideo.mp4')

# Reading video frame by frame
while True:
    # return the frame and boolean if the reading success
    isTrue, frame = capture.read()
    # display each frame
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

# cv.imshow('Dog', img)
# cv.waitKey(0)
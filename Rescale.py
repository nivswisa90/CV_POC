import cv2 as cv

img = cv.imread('./Pictures/dog1.jpg')
cv.imshow('Dog', img)


# Modify height and width to particular height and width works for Images Vidoes & Live videos
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# Option to resize picture as well
resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)


# another way to resize with the method capture.set for Live Video
def changeRes(width, height):

    # 3 - refs width
    capture.set(3, width)

    # 4 - refs Height
    capture.set(4, height)


# Reading video
capture = cv.VideoCapture('./Video/dogVideo.mp4')

# Reading video frame by frame
while True:
    # return the frame and boolean if the reading success
    isTrue, frame = capture.read()

    # display each frame
    frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)

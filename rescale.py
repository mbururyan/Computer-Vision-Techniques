import cv2 as cv

# Read img file

# img1 = cv.imread('pics/dog3.jpeg')

# cv.imshow('dog pic', img1)

# rescaling

def rescaleFrame(frame, scale = 0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)


# Play video with rescaled vid

capture_vid = cv.VideoCapture('videos/Cute Cat - 3092.mp4')

while True:
    isTrue, frame = capture_vid.read()
# define resized frame
    frame_resized = rescaleFrame(frame)

    cv.imshow('OG  video', frame)
    cv.imshow('Resized Video', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break


capture.release()
cv.destroyAllWindows()
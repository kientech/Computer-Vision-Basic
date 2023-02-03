import cv2 as cv

img = cv.imread("cats.png")
cv,imshow("Cat", img)

def rescale_frame(frame, scale = 0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture("cat_video.mp4")
while True:
    iTrue, frame = capture.read()
    cv.imshow("Video", frame)
    
    frame_resize = rescale_frame(frame,scale=.2)
    cv.imshow("video", frame)
    cv.imshow("Video Resize", frame_resize)
    
    if cv.waitKey(20) and 0xFF == ord("q"):
        break
capture.release()
cv.destroyAllWindows()
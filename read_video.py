import cv2 as cv

capture = cv.VideoCapture("cat_video.mp4")
while True:
    iTrue, frame = capture.read()
    cv.imshow("Video", frame)
    
    if cv.waitKey(20) and 0xFF == ord("q"):
        break
    

capture.release()
cv.destroyAllWindows()
import cv2 as cv

img = cv.imread("cats.png")
cv.imshow("Cat", img)

def rescale_frame(frame, scale = 0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


resized_img = rescale_frame(img)
cv.imshow("Image", resized_img)
cv.waitKey(0)
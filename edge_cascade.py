import cv2 as cv

img = cv.imread("cats.png")
cv.imshow("Cat", img)

canny = cv.Canny(img, 125, 175)
cv.imshow("Canny", canny)

cv.waitKey(0)
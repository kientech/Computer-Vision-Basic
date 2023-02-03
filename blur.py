import cv2 as cv

img = cv.imread("cats.png")
cv.imshow("Cat", img)

blur = cv.GaussianBlur(img, (9,9), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

cv.waitKey(0)
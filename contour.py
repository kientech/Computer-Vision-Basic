import cv2 as cv

img = cv.imread("cats.png")
cv.imshow("Cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)

canny = cv.Canny(img, 125, 255)
cv.imshow("Canny", canny)
cv.waitKey(0)
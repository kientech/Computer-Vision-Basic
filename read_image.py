import cv2 as cv

img = cv.imread('cats.png') # export image path
cv.imshow("cats", img)

cv.waitKey(0)
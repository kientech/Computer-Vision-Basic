import cv2 as cv
import numpy as np

img = cv.imread("cats")
cv.imshow("Cats", img)


b, g, r = cv.split(img)
cv.imshow("B", b)
cv.imshow("G", g)
cv.imshow("R", r)

blank = np.zeros(img.shape[:2], dtype="uint8")
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, b, blank])
red = cv.merge([blank, blank, b])

cv.imshow("Blue", blue)
cv.imshow("Red", red)
cv.imshow("Green", green)

print(img.shape)  # (1060, 1884, 3) = (width , height, depth)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b, g, r])
cv.imshow("Merged Image", merged)

cv.waitKey(0)

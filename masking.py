import cv2 as cv
import numpy as np

img = cv.imread("cats.png")
cv.imshow("Cats", img)

# img.shape = (1060, 1884, 3)
blank = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("Blanks", blank)

masked = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow("Masked", masked)

cv.waitKey(0)
import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype = 'uint8') # width, height, number of color = 3
cv.imshow("Blank", blank)

cv.circle(blank, (250,250), 40, (0, 250, 0), thickness=-1)
cv.imshow("Circle",blank)

cv.waitKey(0)
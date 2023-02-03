import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype = 'uint8') # width, height, number of color = 3
cv.imshow("Blank", blank)

cv.line(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=3)
cv.imshow("Line",blank)

cv.waitKey(0)
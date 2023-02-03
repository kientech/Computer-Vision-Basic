import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype = 'uint8') # width, height, number of color = 3
cv.imshow("Blank", blank)

blank[:] = 0, 255, 0
cv.imshow("Green", blank)
cv.waitKey(0)
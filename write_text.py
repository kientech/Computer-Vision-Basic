import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype = 'uint8') # width, height, number of color = 3
cv.imshow("Blank", blank)

cv.putText(blank, "Hello, My name is Kien", (0, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 250, 0), 2)
cv.imshow("Line",blank)

cv.waitKey(0)
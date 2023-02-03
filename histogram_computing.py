import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("cats.png")
cv.imshow("Cats", img)

gray =  cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# grayscale histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])
plt.figure()
plt.title("Histogram Grayscale")
plt.xlabel("Bins")
plt.ylabel("# of bins")
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()
cv.waitKey(0)
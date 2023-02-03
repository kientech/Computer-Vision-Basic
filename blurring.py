import cv2 as cv 

img = cv.imread("cats.png")
cv.imshow("Cats", img)

# Averaging
averate = cv.blur(img, (7, 7))
cv.imshow("Averaging", averate)

# Gaussian Blur
gaussian = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow("Gaussian Blur", gaussian)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow("Median Blur", median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("Bilateral", bilateral)
cv.waitKey(0)
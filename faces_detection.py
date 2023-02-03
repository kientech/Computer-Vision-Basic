import cv2 as cv

# read image
img = cv.imread("./data/3-people.jpg")
cv.imshow("Messi", img)

# grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)


haar_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=6)
print(len(faces_rect))
for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv.imshow("Face Detection", img)

cv.waitKey(0)
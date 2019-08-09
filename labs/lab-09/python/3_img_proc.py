import cv2
import numpy

SOURCE = "pants"

img = cv2.imread("../img/" + SOURCE + ".jpg")
img = cv2.resize(img, dsize=(28, 28))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("../img/" + SOURCE + "_proc.jpg", img)

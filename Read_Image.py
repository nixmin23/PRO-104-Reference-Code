import cv2
import numpy

img = cv2.imread("color.png")

gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

cv2.imshow("output",img)
cv2.imshow("Grayscale",gray)

print(img.shape)
print(gray.shape)

cv2.waitKey(0)










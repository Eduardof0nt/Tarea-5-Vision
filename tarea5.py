import cv2
import numpy as np

img = cv2.imread('tarea5.png', cv2.IMREAD_GRAYSCALE)

_,thresh = cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)

kernel = np.ones((5,5),np.uint8)

threshC = cv2.morphologyEx(thresh.copy(), cv2.MORPH_CLOSE, kernel)

img2 = threshC.copy()

size = np.size(img)
skeleton = np.zeros(thresh.shape, np.uint8)

element = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

while True:
    eroded = cv2.erode(img2,element)
    temp = cv2.dilate(eroded,element)
    temp = cv2.subtract(img2,temp)
    skeleton = cv2.bitwise_or(skeleton,temp)
    img2 = eroded.copy()

    zeros = size - cv2.countNonZero(img2)
    if zeros==size:
        break

cv2.imshow("Imagen original", threshC)
cv2.imshow("Imagen esqueletonizada", skeleton)
cv2.waitKey(0)
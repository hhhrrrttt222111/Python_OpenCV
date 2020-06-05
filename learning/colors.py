import cv2
import numpy as np

img = cv2.imread('../images/xWPH06Gr.jpg')
B, G, R = cv2.split(img)

cv2.imshow('original', img)
cv2.waitKey(0)

cv2.imshow('blue', B)
cv2.waitKey(0)

cv2.imshow('Green', G)
cv2.waitKey(0)

cv2.imshow('red', R)
cv2.waitKey(0)

cv2.destroyAllWindows()
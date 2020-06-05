import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../images/wolverine-hugh-jackman-x-men-hd-wallpapers-collection-8.jpg')

(height, width) = img.shape[:2]

M = cv2.getRotationMatrix2D((int(width/2), int(height/2)), 45, 1)
res = cv2.warpAffine(img, M, (height, width))

cv2.imshow('resized', res)
cv2.waitKey(0)

edges = cv2.Canny(img, 10, 200)
cv2.imshow('resized', edges)
cv2.waitKey(0)
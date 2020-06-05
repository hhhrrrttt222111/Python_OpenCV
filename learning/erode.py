import cv2
import numpy as np

img = cv2.imread('../images/xWPH06Gr.jpg')

# kernel1 = np.ones((5,5), np.uint8)
# img1 = cv2.erode(img, kernel1)

# cv2.imshow('Eroded', img1)
# cv2.waitKey(0)

kernel2 = np.ones((6,6), np.uint8)
img2 = cv2.erode(img, kernel2, cv2.BORDER_REFLECT)
cv2.imshow('Eroded', img2)
cv2.waitKey(0)
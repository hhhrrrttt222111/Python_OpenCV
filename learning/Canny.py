import cv2
import numpy as np


img1 = cv2.imread('../images/civil2.jpg')


canny = cv2.Canny(img1, 100,200)
cv2.imshow('Canny', canny)
cv2.waitKey(0)

cv2.destroyAllWindows()
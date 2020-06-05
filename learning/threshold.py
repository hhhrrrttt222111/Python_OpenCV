import cv2
import numpy as np


image = cv2.imread('../images/electrical2.jpg')

img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
# ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
# ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
# ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
# ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)
#
# cv2.imshow('Binary Threshold', thresh1)
# cv2.waitKey(0)
#
# cv2.imshow('Binary Threshold Inverted', thresh2)
# cv2.waitKey(0)
#
# cv2.imshow('Truncated Threshold', thresh3)
# cv2.waitKey(0)
#
# cv2.imshow('Set to 0', thresh4)
# cv2.waitKey(0)
#
# cv2.imshow('Set to 0 Inverted', thresh5)
# cv2.waitKey(0)


# thresh6 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 119, 5)
# thresh7 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 119, 5)
#
# cv2.imshow('Mean', thresh6)
# cv2.waitKey(0)
# cv2.imshow('Mean', thresh7)
# cv2.waitKey(0)

ret, thresh8 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('Otsu', thresh8)
cv2.waitKey(0)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
import cv2
import numpy as np

img = cv2.imread('../images/p2049927-avengers-infinity-war-wallpapers.jpg')
img1 = cv2.imread('../images/civil5.jpg')

# cv2.imshow('original', img)
cv2.waitKey(0)

gaussian = cv2.GaussianBlur(img, (7,7), 0)
# cv2.imshow('Gaussian Blur', gaussian)
cv2.waitKey(0)

median = cv2.medianBlur(img, 5)
# cv2.imshow('Median Blur', median)
cv2.waitKey(0)

bil = cv2.bilateralFilter(img, 9, 75, 75)
# cv2.imshow('Bilateral Blurring', bil)
cv2.waitKey(0)

img = cv2.blur(img, ksize=(15, 15))
# cv2.imshow('Blurring', img)
cv2.waitKey(0)


cv2.destroyAllWindows()
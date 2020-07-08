import cv2
import numpy as np

img = cv2.imread('../images/electrical4.jpg')

hor = np.hstack((img, img))
ver = np.vstack((img, img))

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.imshow("hor image", hor)
cv2.waitKey(0)
cv2.imshow("ver image", ver)
cv2.waitKey(0)
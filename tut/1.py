import cv2
import numpy as np

img = cv2.imread('../images/shapes.png')

imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGrey, (7, 7), 1)


hor = np.hstack((imgBlur, imgGrey))

cv2.imshow("image", hor)
cv2.waitKey(0)

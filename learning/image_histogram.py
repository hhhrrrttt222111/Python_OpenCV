import cv2
from matplotlib import pyplot as plt
import numpy as np


img = cv2.imread('../images/p2049927-avengers-infinity-war-wallpapers.jpg', 0)

# histr = cv2.calcHist([img], [0], None, [256], [0, 256])
#
# plt.plot(histr)
# plt.show()


equ = cv2.equalizeHist(img)

res = np.hstack((img, equ))

cv2.imshow('images', res)
cv2.waitKey(0)
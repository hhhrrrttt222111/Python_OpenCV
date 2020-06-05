import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../images/electrical2.jpg')

dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 15)

plt.subplot(121), plt.imshow(img)
plt.subplot(122), plt.imshow(dst)

plt.show()


import cv2
import numpy as np

img = cv2.imread('../images/black-spiderman-wallpaper-free.jpg', 1)

cv2.imshow('spidey', img)
k = cv2.waitKey(0) & 0xFF

if k == 27:
    cv2.destroyAllWindows()

elif k == ord('s'):
    cv2.imwrite('spideyGRAY.png', img)
    cv2.destroyAllWindows()
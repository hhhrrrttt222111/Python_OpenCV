import cv2
import numpy as np

img1 = cv2.imread('../images/ron-man-jarvis-wallpapers-high-quality.jpg')
img2 = cv2.imread('../images/black-spiderman-wallpaper-free.jpg')


sum = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

cv2.imshow('Added', sum)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()



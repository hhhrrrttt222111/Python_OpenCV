import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('../images/civil5.jpg')

grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('grey', grey_img)
cv2.waitKey(0)




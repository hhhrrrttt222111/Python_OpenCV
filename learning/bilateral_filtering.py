import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('../images/electrical4.jpg')

bil = cv2.medianBlur(img, (15, 15))

cv2.imshow('wow', bil)
cv2.waitKey(0)
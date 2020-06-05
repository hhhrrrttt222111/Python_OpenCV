import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


# img = cv2.imread('../images/ienom.jpg')
#
# blur_img1 = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT)
# blur_img2 = cv2.copyMakeBorder(img, 200, 200, 50, 50, cv2.BORDER_REFLECT)
#
# cv2.imshow('blurred image 1', blur_img1)
# cv2.waitKey(0)
#
# cv2.imshow('blurred image 2', blur_img2)
# cv2.waitKey(0)


BLUE = [255,0,0]
img1 = cv.imread('../images/ienom.jpg')
replicate = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_WRAP)
constant= cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_CONSTANT,value=BLUE)
plt.subplot(231), plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()
import cv2
import matplotlib.pyplot as plt


img = cv2.imread('../images/electrical4.jpg')

start = (0, 0)
end = (250, 250)

color = (120, 55, 56)

image = cv2.line(img, start, end, color, 5)
image_arrow = cv2.arrowedLine(img, start, end, color, 5)

cv2.imshow('image', image)
cv2.waitKey(0)
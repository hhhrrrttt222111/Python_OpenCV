import cv2


image = cv2.imread('../images/wolverine-hugh-jackman-x-men-hd-wallpapers-collection-8.jpg')

center_coordinates = (620, 430)
axesLength = (800, 520)
angle = 0
startAngle = 0
endAngle = 360
color = (0, 255, 155)
thickness = 41

image = cv2.ellipse(image, center_coordinates, axesLength,
                    angle, startAngle, endAngle, color, thickness)

cv2.imshow('ellipse', image)
cv2.waitKey(0)

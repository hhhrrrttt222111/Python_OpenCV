import numpy as np
import cv2

img = np.zeros((500, 500, 3), dtype="uint8")

cv2.line(img, (20, 160), (100, 160), (0, 0, 255), 10)
cv2.rectangle(img, (30, 30), (300, 200), (0, 255, 0), 5)
cv2.circle(img, (200, 200), 80, (255, 0, 0), 3)
cv2.putText(img, 'HRT', (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (100, 155, 100), 2, cv2.LINE_AA)

p1 = (100, 200)
p2 = (50, 50)
p3 = (300, 100)


cv2.line(img, p1, p2, (25, 100, 150), 3)
cv2.line(img, p2, p3, (25, 100, 150), 3)
cv2.line(img, p1, p3, (25, 100, 150), 3)

centroid = ((p1[0] + p2[0] + p3[0]) // 3, (p1[1] + p2[1] + p3[1]) // 3)

cv2.circle(img, centroid, 4, (0, 255, 0))

cv2.imshow('dark', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

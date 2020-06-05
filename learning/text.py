import cv2

path = r'../images/xWPH06Gr.jpg'


image = cv2.imread(path)

text = 'GeeksforGeeks'
font = cv2.FONT_HERSHEY_SIMPLEX
org = (00, 185)
fontScale = 1
color = (0, 0, 255)
thickness = 2

image = cv2.putText(image, text, org, font, fontScale,
                    (25,21,56), thickness, cv2.LINE_AA, True)

# Using cv2.putText() method
image = cv2.putText(image, text, org, font, fontScale,
                    color, thickness, cv2.LINE_AA, False)

# Displaying the image
cv2.imshow('window_name', image)
cv2.waitKey(0)

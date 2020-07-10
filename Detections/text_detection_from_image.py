from imutils.object_detection import non_max_suppression
import numpy as np
import argparse
import time
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, help="path to input image")
ap.add_argument("-east", "--east", type=str, help="path to input EAST text detector")
ap.add_argument("-c", "--min-confidence", type=float, default=0.5, help="minimum probability required to inspect a region")
ap.add_argument("-w", "--width", type=int, default=320, help="resized image width (should be multiple of 32)")
ap.add_argument("-e", "--height", type=int, default=320, help="resized image height (should be multiple of 32)")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
orig = image.copy()
(H, W) = image.shape[:2]

(newW, newH) = (args["width"], args["height"])
rW = W / float(newW)
rH = H / float(newH)

image = cv2.resize(image, (newW, newH))
(H, W) = image.shape[:2]

layerNames = [
	"feature_fusion/Conv_7/Sigmoid",
	"feature_fusion/concat_3"]

print("[INFO] loading EAST text detector...")
net = cv2.dnn.readNet(args["east"])

blob = cv2.dnn.blobFromImage(image, 1.0, (W, H), (123.68, 116.78, 103.94), swapRB=True, crop=False)
start = time.time()
net.setInput(blob)
(scores, geometry) = net.forward(layerNames)
end = time.time()

print("[INFO] text detection took {:.6f} seconds".format(end - start))

(numRows, numCols) = scores.shape[2:4]
rects = []
confidences = []

for y in range(0, numRows):

	scoresData = scores[0, 0, y]
	xData0 = geometry[0, 0, y]
	xData1 = geometry[0, 1, y]
	xData2 = geometry[0, 2, y]
	xData3 = geometry[0, 3, y]
	anglesData = geometry[0, 4, y]


	for x in range(0, numCols):
		# if our score does not have sufficient probability, ignore it
		if scoresData[x] < args["min_confidence"]:
			continue
		(offsetX, offsetY) = (x * 4.0, y * 4.0)
		angle = anglesData[x]
		cos = np.cos(angle)
		sin = np.sin(angle)

		h = xData0[x] + xData2[x]
		w = xData1[x] + xData3[x]

		endX = int(offsetX + (cos * xData1[x]) + (sin * xData2[x]))
		endY = int(offsetY - (sin * xData1[x]) + (cos * xData2[x]))
		startX = int(endX - w)
		startY = int(endY - h)

		rects.append((startX, startY, endX, endY))
		confidences.append(scoresData[x])


boxes = non_max_suppression(np.array(rects), probs=confidences)

for (startX, startY, endX, endY) in boxes:

	startX = int(startX * rW)
	startY = int(startY * rH)
	endX = int(endX * rW)
	endY = int(endY * rH)

	cv2.rectangle(orig, (startX, startY), (endX, endY), (0, 255, 0), 2)

cv2.imshow("Text Detection", orig)
cv2.waitKey(0)
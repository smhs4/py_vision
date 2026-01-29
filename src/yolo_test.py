from ultralytics import YOLO
import cv2

img = cv2.imread("person.jpg")
model = YOLO("yolov8n-seg.pt")
results = model(img)
vis = results[0].plot()
cv2.imshow("Test", vis)
cv2.waitKey(0)

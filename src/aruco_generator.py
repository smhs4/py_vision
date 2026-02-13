import cv2

aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
side_px = 800
for i in range(10):
    marker_id = 2*i
    img = cv2.aruco.generateImageMarker(aruco_dict, marker_id, side_px)
    dest = f"markers/marker_{marker_id}.png"
    cv2.imwrite(dest, img)
    print('one image saved')

    
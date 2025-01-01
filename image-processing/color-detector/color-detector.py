import cv2
import numpy as np

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    if not ret:
        print("Fail")
        break


    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([0, 140, 40])
    upper_red1 = np.array([6, 255, 255])
    lower_red2 = np.array([172, 140, 40])
    upper_red2 = np.array([180, 255, 255])

    mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask_red = cv2.bitwise_or(mask_red1, mask_red2)
    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours_red:
        if cv2.contourArea(contour) > 300:
            cv2.drawContours(frame, [contour], -1, (0, 0, 255), 2)


    lower_green = np.array([48, 40, 25])
    upper_green = np.array([78, 255, 255])
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    contours_green, _ = cv2.findContours(mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours_green:
        if cv2.contourArea(contour) > 300:
            cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)


    lower_blue = np.array([94, 40, 1])
    upper_blue = np.array([130, 255, 220])
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours_blue:
        if cv2.contourArea(contour) > 300:
            cv2.drawContours(frame, [contour], -1, (255, 0, 0), 2)

    cv2.imshow('Frame', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


capture.release()
cv2.destroyAllWindows()
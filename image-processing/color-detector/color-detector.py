import cv2
import numpy as np

capture = cv2.VideoCapture(0)

def display_color_box(frame, hsv_color, position):
    color_array = np.array([[hsv_color]], dtype=np.uint8)
    bgr = cv2.cvtColor(color_array, cv2.COLOR_HSV2BGR)
    color = tuple(map(int, bgr[0][0]))
    x, y = position
    cv2.rectangle(frame, (x, y), (x + 20, y + 20), color, -1)

while True:
    ret, frame = capture.read()
    if not ret:
        print("Fail")
        break

    frame = cv2.flip(frame, 1)
    cv2.imshow('Original Frame', frame)

    frame = cv2.GaussianBlur(frame, (3, 3), sigmaX = 7)
    frame = cv2.medianBlur(frame, 3)
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    kernel = np.ones((5,5), np.uint8)
    

    lower_red1 = np.array([172, 140, 100])
    upper_red1 = np.array([180, 255, 255])
    lower_red2 = np.array([0, 140, 100])
    upper_red2 = np.array([6, 255, 255])
    
    mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask_red = cv2.bitwise_or(mask_red1, mask_red2)
    mask_red = cv2.morphologyEx(mask_red, cv2.MORPH_OPEN, kernel)
    mask_red = cv2.morphologyEx(mask_red, cv2.MORPH_CLOSE, kernel)
    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours_red:
        if cv2.contourArea(contour) > 200:
            cv2.drawContours(frame, [contour], -1, (0, 0, 255), 2)


    lower_green = np.array([48, 40, 60])
    upper_green = np.array([80, 255, 255])
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    contours_green, _ = cv2.findContours(mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours_green:
        if cv2.contourArea(contour) > 200:
            cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)


    lower_blue = np.array([110, 50, 40])
    upper_blue = np.array([132, 255, 255])
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours_blue:
        if cv2.contourArea(contour) > 200:
            cv2.drawContours(frame, [contour], -1, (255, 0, 0), 2)

    # Display color boxes for all ranges
    display_color_box(frame, lower_red1, (10, 10))
    display_color_box(frame, upper_red1, (40, 10))
    display_color_box(frame, lower_red2, (70, 10))
    display_color_box(frame, upper_red2, (100, 10))
    
    display_color_box(frame, lower_green, (130, 10))
    display_color_box(frame, upper_green, (160, 10))
    
    display_color_box(frame, lower_blue, (190, 10))
    display_color_box(frame, upper_blue, (220, 10))

    cv2.imshow('Frame', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


capture.release()
cv2.destroyAllWindows()
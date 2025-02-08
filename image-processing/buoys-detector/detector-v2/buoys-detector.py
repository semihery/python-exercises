import cv2
import numpy as np


COLOR_RANGES = {
    'red': {
        'ranges': [
            ([0, 50, 100], [10, 255, 255]),
            ([170, 50, 100], [180, 255, 255])
        ]
    } #,
    # 'yellow': {
    #     'ranges': [([10, 90, 100], [30, 255, 255])]
    # },
    # 'green': {
    #     'ranges': [([50, 160, 70], [100, 255, 255])]
    # },
    # 'black': {
    #     'ranges': [([0, 0, 0], [180, 255, 38])]
    # },
    # 'orange': {
    #     'ranges': [([10, 100, 80], [20, 255, 255])]
    # }
}

image = cv2.imread('img.jpg')
if image is None:
    print("img not found")
    exit()


blurred = cv2.GaussianBlur(image, (9, 9), sigmaX=2)


hsv_blurred = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
blue_lower = np.array([90, 20, 0])
blue_upper = np.array([130, 255, 255])

#mavi renk aralığını silme
blue_mask = cv2.inRange(hsv_blurred, blue_lower, blue_upper)
hsv_blurred[blue_mask > 0] = [0, 0, 0]
# cv2.imshow('blur', cv2.cvtColor(hsv_blurred, cv2.COLOR_HSV2BGR))

h, s, v = cv2.split(cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV))

h[(h > 8) & (h < 175)] = 30
h = (h + 150) % 180

v[v < 240] = 0
kernel = np.ones((4,4), np.uint8)

v = cv2.morphologyEx(v, cv2.MORPH_CLOSE, kernel)
v = cv2.erode(v, kernel, iterations=2)
v = cv2.morphologyEx(v, cv2.MORPH_OPEN, kernel)
contours, _ = cv2.findContours(v, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    if cv2.contourArea(contour) < 400:
        cv2.drawContours(v, [contour], -1, 0, -1)
v = cv2.dilate(v, kernel, iterations=2)
v = cv2.morphologyEx(v, cv2.MORPH_CLOSE, kernel)

cv2.imshow('Hue Channel', h)
cv2.imshow('Saturation Channel', s)
cv2.imshow('Value Channel', v)



def create_color_mask(hsv_img, color_name):
    mask = np.zeros(hsv_img.shape[:2], dtype=np.uint8)
    for lower, upper in COLOR_RANGES[color_name]['ranges']:
        color_mask = cv2.inRange(hsv_img, np.array(lower), np.array(upper))
        mask = cv2.bitwise_or(mask, color_mask)
    return mask


def is_buoy(contour):
    
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)
    if perimeter == 0:
        return False
    circularity = 4 * np.pi * area / (perimeter * perimeter)
    
    
    return 0.2 < circularity < 1.2 and area > 1000


for color_name in COLOR_RANGES:
    
    mask = create_color_mask(hsv_blurred, color_name)

    # cv2.imshow(f'{color_name} mask', mask)
    
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    
    for contour in contours:
        if is_buoy(contour):
            
            x, y, w, h = cv2.boundingRect(contour)
            
            
            center_x = x + w//2
            center_y = y + h//2
            
            
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.circle(image, (center_x, center_y), 3, (0, 0, 255), -1)
            
            
            cv2.putText(image, f"{color_name} buoy", (x, y-10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


cv2.imshow('Detected Buoys', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
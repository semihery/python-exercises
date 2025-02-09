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

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (6, 6))
h, s, v = cv2.split(cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV))

# Create a mask for hues close to red (near 0° or near 180°)
low_red = h < 10
high_red = h > 175
# For pixels not in the red area, set hue to 30 (a placeholder value)
h[~(low_red | high_red)] = 30
# Shift hue values so that the red pixels wrap continuously:
# Convert h to int32 to avoid overflow issues.
h = ((h.astype(np.int32) + 150) % 180).astype(np.uint8)
h = cv2.morphologyEx(h, cv2.MORPH_CLOSE, kernel)

s[h == 0] = 0
s[(s) > 10] = 255
s = cv2.morphologyEx(s, cv2.MORPH_CLOSE, kernel)

v[v < 240] = 0
v = cv2.morphologyEx(v, cv2.MORPH_CLOSE, kernel)
v = cv2.erode(v, kernel, iterations=2)
v = cv2.morphologyEx(v, cv2.MORPH_OPEN, kernel)
contours, _ = cv2.findContours(v, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    if cv2.contourArea(contour) < 400:
        cv2.drawContours(v, [contour], -1, 0, -1)
v = cv2.dilate(v, kernel, iterations=2)
v = cv2.morphologyEx(v, cv2.MORPH_CLOSE, kernel)

_, v = cv2.threshold(v, 200, 255, cv2.THRESH_BINARY)

# buoy_bottoms = []

# for contour in contours:
#     # Find the lowest y-coordinate for each buoy
#     lowest_y = max(point[0][1] for point in contour)
    
#     # Collect all contour points with this y-coordinate
#     bottom_points = [point[0] for point in contour if (lowest_y - point[0][1]) < 20]
    
#     # Compute the average y of these bottom points
#     avg_y = sum(p[1] for p in bottom_points) / len(bottom_points)
#     buoy_bottoms.append(avg_y)

#     def draw_dashed_line(img, pt1, pt2, color, thickness=2, dash_length=10, gap_length=5):
#         x1, y1 = pt1
#         x2, y2 = pt2
#         line_length = int(np.hypot(x2 - x1, y2 - y1))
#         if line_length == 0:
#             return
#         for i in range(0, line_length, dash_length + gap_length):
#             start_ratio = i / line_length
#             end_ratio = min(1, (i + dash_length) / line_length)
#             sx = int(x1 + (x2 - x1) * start_ratio)
#             sy = int(y1 + (y2 - y1) * start_ratio)
#             ex = int(x1 + (x2 - x1) * end_ratio)
#             ey = int(y1 + (y2 - y1) * end_ratio)
#             cv2.line(img, (sx, sy), (ex, ey), color, thickness)

#     # Draw a horizontal dashed line on each buoy bottom
#     height, width = image.shape[:2]
#     for y in buoy_bottoms:
#         y = int(y)
#         start_point = (10, y)
#         end_point = (width - 10, y)
#         draw_dashed_line(image, start_point, end_point, (255, 0, 0), thickness=2, dash_length=15, gap_length=10)

cv2.imshow('Hue Channel', h)
cv2.imshow('Saturation Channel', s)
cv2.imshow('Value Channel', v)


def is_circular(contour):    
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)
    if perimeter == 0:
        return False
    circularity = 4 * np.pi * area / (perimeter * perimeter)
    
    return 0.2 < circularity < 1.2 and area > 1000

def calculate_buoy_distance(y, camera_angle=-15, camera_fov=30, camera_height=150, image_height=1080):
    """
    Calculate the distance to a buoy based on its vertical position in the image.
    
    Args:
        y: vertical position of the buoy in the image (pixels from top, increasing downward)
        camera_angle: downward tilt angle of camera in degrees (negative for downward)
        camera_fov: vertical field of view of the camera in degrees
        camera_height: height of the camera from water level in cm
        image_height: height of the image in pixels
    """
    # Convert angles to radians
    camera_angle_rad = np.radians(camera_angle)
    
    # Calculate the angle from image top to target
    # Since y increases downward, we need to adjust how we calculate the relative angle
    pixels_per_degree = image_height / camera_fov
    
    # Convert y position to angle relative to image center
    # Subtract from image_height to flip the coordinate system
    rel_angle = ((image_height - y) - (image_height / 2)) / pixels_per_degree
    rel_angle_rad = np.radians(rel_angle)
    
    # Calculate actual angle to target
    target_angle_rad = -camera_angle_rad - rel_angle_rad
    
    # Prevent division by zero and invalid angles
    if target_angle_rad <= 0:
        return float('inf')
    
    # Calculate distance using tangent
    distance = camera_height / np.tan(target_angle_rad)
    
    # Convert to meters
    return distance / 100.0

def draw_dashed_line(img, pt1, pt2, color, thickness=4, dash_length=10, gap_length=5):
    x1, y1 = pt1
    x2, y2 = pt2
    line_length = int(np.hypot(x2 - x1, y2 - y1))
    if line_length == 0:
        return
    for i in range(0, line_length, dash_length + gap_length):
        start_ratio = i / line_length
        end_ratio = min(1, (i + dash_length) / line_length)
        sx = int(x1 + (x2 - x1) * start_ratio)
        sy = int(y1 + (y2 - y1) * start_ratio)
        ex = int(x1 + (x2 - x1) * end_ratio)
        ey = int(y1 + (y2 - y1) * end_ratio)
        cv2.line(img, (sx, sy), (ex, ey), color, thickness)

def draw_bottom_line(contour):
    # Get the center of the original contour
    M = cv2.moments(contour)
    if M["m00"] == 0:
        return
    cx = int(M["m10"] / M["m00"])
    cy = int(M["m01"] / M["m00"])
    
    # Find closest contour in v frame
    v_contours, _ = cv2.findContours(v, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    closest_contour = None
    min_dist = float('inf')
    
    for v_contour in v_contours:
        M = cv2.moments(v_contour)
        if M["m00"] == 0:
            continue
        v_cx = int(M["m10"] / M["m00"])
        v_cy = int(M["m01"] / M["m00"])
        
        dist = np.sqrt((cx - v_cx)**2 + (cy - v_cy)**2)
        if dist < min_dist:
            min_dist = dist
            closest_contour = v_contour
    
    if closest_contour is not None:
        # Process the closest contour from v frame
        lowest_y = max(point[0][1] for point in closest_contour)
        bottom_points = [point[0] for point in closest_contour if (lowest_y - point[0][1]) < 20]
        if bottom_points:
            avg_y = sum(p[1] for p in bottom_points) / len(bottom_points)
            xs = [point[0][0] for point in closest_contour]
            min_x, max_x = min(xs), max(xs)
            y = int(avg_y)
            draw_dashed_line(image, (min_x, y), (max_x, y), (255, 0, 0), thickness=4, dash_length=15, gap_length=10)

            distance = calculate_buoy_distance(y)
            cv2.putText(image, f"Distance: {distance:.1f}m", (min_x, y+30), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)


combined_mask = cv2.bitwise_or(h, s)

contours, _ = cv2.findContours(combined_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    if is_circular(contour):
      
        x, y, w, h = cv2.boundingRect(contour)
      
      
        center_x = x + w//2
        center_y = y + h//2
      
      
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.circle(image, (center_x, center_y), 3, (0, 255, 0), -1)
      
      
        cv2.putText(image, "red buoy", (x, y-10),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        draw_bottom_line(contour)






# def create_color_mask(hsv_img, color_name):
#     mask = np.zeros(hsv_img.shape[:2], dtype=np.uint8)
#     for lower, upper in COLOR_RANGES[color_name]['ranges']:
#         color_mask = cv2.inRange(hsv_img, np.array(lower), np.array(upper))
#         mask = cv2.bitwise_or(mask, color_mask)
#     return mask



# for color_name in COLOR_RANGES:
    
#     mask = create_color_mask(hsv_blurred, color_name)

#     # cv2.imshow(f'{color_name} mask', mask)
    
#     contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    
#     for contour in contours:
#         if is_circular(contour):
            
#             x, y, w, h = cv2.boundingRect(contour)
            
            
#             center_x = x + w//2
#             center_y = y + h//2
            
            
#             cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
#             cv2.circle(image, (center_x, center_y), 3, (0, 0, 255), -1)
            
            
#             cv2.putText(image, f"{color_name} buoy", (x, y-10),
#                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


cv2.imshow('Detected Buoys', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
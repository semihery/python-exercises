import cv2
import numpy as np

def get_dominant_color(cell_hsv):
    # Flatten the cell to 2D array of pixels
    pixels = cell_hsv.reshape(-1, 3)
    
    # Convert to 8-bit integers for better clustering
    pixels = np.float32(pixels)
    
    # Define criteria for k-means
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    
    # Apply k-means clustering to find dominant color
    _, labels, centers = cv2.kmeans(pixels, 1, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    
    # Get the dominant color
    dominant_color = centers[0]
    
    # Count number of non-black and non-white pixels
    valid_pixels = np.sum(np.logical_and(pixels[:, 1] > 50, pixels[:, 2] > 50))
    total_pixels = pixels.shape[0]
    
    # Return dominant color only if enough valid pixels
    if valid_pixels / total_pixels > 0.3:
        return dominant_color
    return None

def detect_objects():
    cap = cv2.VideoCapture(0)
    grid_size = (6, 6)  # Smaller grid for real-time processing
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        # Convert frame to HSV
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        blur = cv2.GaussianBlur(hsv_frame, (11, 11), 0)
        
        # Get frame dimensions and cell sizes
        height, width = frame.shape[:2]
        cell_height = height // grid_size[0]
        cell_width = width // grid_size[1]
        
        # Create combined mask
        combined_mask = np.zeros((height, width), dtype=np.uint8)
        
        # Analyze each cell
        for i in range(grid_size[0]):
            for j in range(grid_size[1]):
                # Extract cell
                cell = blur[i*cell_height:(i+1)*cell_height,
                          j*cell_width:(j+1)*cell_width]
                
                # Get dominant color in cell
                dominant_color = get_dominant_color(cell)
                if dominant_color is not None:
                    # Create color range for detection
                    color_range = 30
                    lower = np.array([max(0, dominant_color[0] - color_range),
                                    max(0, dominant_color[1] - color_range),
                                    max(0, dominant_color[2] - color_range)], dtype=np.uint8)
                    upper = np.array([min(180, dominant_color[0] + color_range),
                                    min(255, dominant_color[1] + color_range),
                                    min(255, dominant_color[2] + color_range)], dtype=np.uint8)
                    
                    # Create mask for current cell
                    cell_mask = cv2.inRange(cell, lower, upper)
                    combined_mask[i*cell_height:(i+1)*cell_height,
                                j*cell_width:(j+1)*cell_width] = cell_mask
                    
                    # Draw grid cell for visualization
                    cv2.rectangle(frame, (j*cell_width, i*cell_height),
                                ((j+1)*cell_width, (i+1)*cell_height),
                                (0, 255, 0), 1)
        
        # Process mask
        kernel = np.ones((5,5), np.uint8)
        mask = cv2.morphologyEx(combined_mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        
        # Find contours
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Draw contours
        for contour in contours:
            if cv2.contourArea(contour) > 500:
                cv2.drawContours(frame, [contour], -1, (255, 0, 0), 2)
        
        # Show frames
        cv2.imshow('Object Detection', frame)
        cv2.imshow('Mask', mask)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Gray', gray)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

detect_objects()
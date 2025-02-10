# Buoys Detector

This project uses Python and OpenCV for detecting buoys in images. The main script, `buoys-detector.py`, processes an input image (`img.jpg`) to identify red buoys based on their color and shape.

## Features

- **Image Preprocessing:** Gaussian blur, HSV conversion, and morphological operations.
- **Buoy Detection:** Contour analysis to identify circular shapes.
- **Distance Calculation:** Estimates buoy distance using camera parameters and image position.
- **Visualization:** Annotates detected buoys with bounding boxes, labels, and dashed lines.

## Prerequisites

- Python 3.x
- OpenCV (`cv2`)
- NumPy


## Customization

- This code is specifically designed for detecting red buoys and is not intended for detecting other colors.
- Customizing the `COLOR_RANGES` dictionary or tuning morphological kernel sizes and thresholds for different buoy colors would require significant modifications to the codebase.

## License

This project is provided for educational purposes. Modify and use it as needed.
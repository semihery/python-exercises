import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Get frame dimensions
        height, width = gray.shape

        # Iterate over center pixels of 25x25 areas
        for y in range(22, height-22, 25):
            for x in range(22, width-22, 25):
                center_pixel = gray[y, x]
                # Draw a point at center pixel for visualization
                cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)

                # Get 25x25 area around center pixel
                area = gray[y-22:y+23, x-22:x+23]
                # Calculate mean difference between center pixel and surrounding pixels
                diff = np.abs(area - center_pixel)
                mean_diff = np.mean(diff) / (np.mean(center_pixel))**1.25 * 100
                # If mean difference is small, pixels are similar
                if mean_diff < 40:  # threshold can be adjusted
                    cv2.rectangle(frame, (x-22, y-22), (x+22, y+22), (255, 0, 0), 1)


        cv2.imshow("Object Detector", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
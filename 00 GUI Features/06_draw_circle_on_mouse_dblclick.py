import numpy as np
import cv2

HEIGHT = 512 # pixels
WIDTH = 512 # pixels
CHANNELS = 3

COLOR_BLUE = (255, 0, 0)

WINDOW_NAME = "Double-Click to Draw Circle"

def mouse_callback(event, x, y, flags, params):


    # Check if the mouse event was a double click
    if event == cv2.EVENT_LBUTTONDBLCLK:

        # Draw a circle
        cv2.circle(img, (x,y), 30, COLOR_BLUE, -1)

    
# Create a window to display the image and capture mouse callbacks
cv2.namedWindow(WINDOW_NAME)
cv2.setMouseCallback(WINDOW_NAME, mouse_callback)

# Create a black image
img = np.zeros((HEIGHT, WIDTH, CHANNELS), np.uint8)


while True:
    # Display the image
    cv2.imshow(WINDOW_NAME, img)

    # Check for key-press to detect if we need to close the window
    k = cv2.waitKey(20) & 0xFF

    # 27 is the ASCII code for ESC key
    if k == ord('q') or k == 27:
        break

# Cleanup
cv2.destroyAllWindows()

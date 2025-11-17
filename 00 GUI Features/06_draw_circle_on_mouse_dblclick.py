'''
This file acts as supplementary material for 00_Getting_Started.ipynb
'''


import numpy as np
import cv2

HEIGHT = 512 # pixels
WIDTH = 512 # pixels
CHANNELS = 3

COLOR_BLUE = (255, 0, 0)

WINDOW_NAME = "Double-Click to Draw Circle"

# Create a mouse callback function
# This has a specific format (args) but we can define the
# function any way we want
def mouse_callback(event, x, y, flags, params):

    # If the mouse event that triggered this callback was a 
    # double-click of the mouse-left button
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

    # cv.waitKey() can return 32-bit or 64-bit integer depending on the architecture
    # This integer can contain additional 'flag' bits in the higher positions 
    # We only care about the last 8 bits, so we do an AND operation with 0xFF
    # This ensures that all bits before the last 8 bits are set to 0.
    k = cv2.waitKey(20) & 0xFF

    # 27 is the ASCII code for ESC key
    if k == ord('q') or k == 27:
        break

# Cleanup
cv2.destroyAllWindows()

'''
This file acts as supplementary material for 00_Getting_Started.ipynb
'''


import numpy as np
import cv2

drawing = False # True if mouse button is pressed
mode = True # If True, draw rectangle, else draw Circle. Press 'm' to toggle modes.

HEIGHT = 512 # pixels
WIDTH = 512 # pixels
CHANNELS = 3
COLOR_BLUE = (255, 0, 0)
WINDOW_NAME = "Press 'm' to switch mode (Rect/Circle)"

ix, iy = -1, -1 # Placeholder to store initial coordinate


# Create a mouse callback function
# This has a specific format (args) but we can define the
# function any way we want
def mouse_callback(event, x, y, flags, params):

    global ix, iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:

        # If button was pressed while mouse was moving
        if drawing == True:

            # Create a temporary copy of the original image to draw the current shape
            temp_image = img.copy()

            # Rectangle mode
            if mode == True:
                cv2.rectangle(temp_image, (ix, iy), (x, y), COLOR_BLUE, 1)
            else:
                radius_vect = [x-ix, y-iy]
                radius = int(np.sqrt(radius_vect[0]**2 + radius_vect[1]**2))
                cv2.circle(temp_image, (ix, iy), radius, COLOR_BLUE, 1)

            # Display temporary image
            cv2.imshow(WINDOW_NAME, temp_image)

    elif event == cv2.EVENT_LBUTTONUP:
        # Upon releasing the button, fix the shape
        drawing = False
        if mode == True:
            cv2.rectangle(img, (ix, iy), (x,y), COLOR_BLUE, 1)
        else:
            radius_vect = [x-ix, y-iy]
            radius = int(np.sqrt(radius_vect[0]**2 + radius_vect[1]**2))
            cv2.circle(img, (ix, iy), radius, COLOR_BLUE, 1)

        # Display the updated main image
        cv2.imshow(WINDOW_NAME, img)


# Create a named window and assign callback to it
cv2.namedWindow(WINDOW_NAME)
cv2.setMouseCallback(WINDOW_NAME, mouse_callback)

# Create a blank image
img = np.zeros((HEIGHT, WIDTH, CHANNELS), np.uint8)

while True:

    # The mouse callback handles imshow() so we don't need to write it here

    # Check for a key-press to detect if we need to close the window or change mode

    # cv.waitKey() can return 32-bit or 64-bit integer depending on the architecture
    # This integer can contain additional 'flag' bits in the higher positions 
    # We only care about the last 8 bits, so we do an AND operation with 0xFF
    # This ensures that all bits before the last 8 bits are set to 0.
    k = cv2.waitKey(20) & 0xFF

    # Check for mode switch
    if k == ord('m'):
        mode = not mode

    # Check for exit condition. 27 is ASCII code for ESC
    if k == ord('q') or k == 27:
        break

# Cleanup
cv2.destroyAllWindows()
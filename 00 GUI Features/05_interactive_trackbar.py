import numpy as np
import cv2


def callback(x):
    '''
    Do Nothing
    '''
    pass

WINDOW_NAME = 'Interactive Window'

HEIGHT = 300
WIDTH = 512
CHANNELS = 3

# Create a window with a black image
cv2.namedWindow(WINDOW_NAME)
img = np.zeros((HEIGHT, WIDTH, CHANNELS), np.uint8)

# Create trackbars for changing the color
# 1st argument : Title of the slider
# 3rd argument : Default INT value >= 0
# 4th argument : Max INT value >= 0
cv2.createTrackbar('R', WINDOW_NAME, 0, 255, callback)
cv2.createTrackbar('G', WINDOW_NAME, 0, 255, callback)
cv2.createTrackbar('B', WINDOW_NAME, 0, 255, callback)

# Create a slider that behaves like a binary switch
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, WINDOW_NAME, 0, 1, callback)

while True:
    # Display the window with the image
    cv2.imshow(WINDOW_NAME, img)

    # Check for Key Press to exit
    k = cv2.waitKey(20) & 0xFF

    # 27 is the ASCII code for ESC key
    if k == ord('q') or k == 27:
        break


    # Get the currente positions of the trackbars
    r = cv2.getTrackbarPos('R', WINDOW_NAME)
    g = cv2.getTrackbarPos('G', WINDOW_NAME)
    b = cv2.getTrackbarPos('B', WINDOW_NAME)
    s = cv2.getTrackbarPos(switch, WINDOW_NAME)

    # Error handling : if the user closes the window by clicking [x] at the window's corner
    # the loop is still running since the termination condition for the loop depends on waitKey
    # As a result, getTrackbarPos will try to access a destroyed window, and return -1
    # To avoid OverflowError, we break the loop if this is detected
    if r < 0 or b < 0 or g < 0:
        break

    # If switch is off, reset the image to black
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

# Cleanup
cv2.destroyAllWindows()
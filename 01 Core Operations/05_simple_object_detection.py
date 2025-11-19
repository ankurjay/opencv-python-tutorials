'''
This file acts as supplementary material for 04_Colorspace_Operations.ipynb
'''

import numpy as np
import cv2


def callback(x):
    '''
    Do Nothing
    '''
    pass

# Create a capture object
cap = cv2.VideoCapture(0)

# If the capture could not be initialized for some reason, exit
if not cap.isOpened():
    print("Cannot open camera!")
    exit()


WINDOW_NAME = 'Object Detection'

# Create a named Window
cv2.namedWindow(WINDOW_NAME)

# Create trackbars for tuning the upper and lower HSV limits
cv2.createTrackbar('Lower Hue', WINDOW_NAME, 0, 178, callback)
cv2.createTrackbar('Upper Hue', WINDOW_NAME, 178, 178, callback)
cv2.createTrackbar('Lower Saturation', WINDOW_NAME, 0, 255, callback)
cv2.createTrackbar('Upper Saturation', WINDOW_NAME, 255, 255, callback)
cv2.createTrackbar('Lower Value', WINDOW_NAME, 0, 255, callback)
cv2.createTrackbar('Upper Value', WINDOW_NAME, 255, 255, callback)

# Create h,s,v limit values
h_upper = 178
h_lower = 0
s_upper = 255
s_lower = 0
v_upper = 255
v_lower = 0


while cap.isOpened():
    
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If the frame is read correctly, ret == true, and 'frame' contains image data
    # Else ret == false, and we need to exit
    if not ret:
        print("Cannot receive frame (stream end?). Exiting...")
        break

    # Frame is read correctly, so do some operations on it
    
    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define range of target color in HSV
    lower_target = np.array([h_lower, s_lower, v_lower]) # Hue, Saturation, Value
    upper_target = np.array([h_upper, s_upper, v_upper]) # Hue, Saturation, Value

    # Threshold the HSV image to only get the target color
    mask = cv2.inRange(hsv, lower_target, upper_target)    

    # Bitwise-AND the mask with the original image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the original video, mask, and masked video 
    cv2.imshow(WINDOW_NAME, frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Object Tracking", res)

    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break


    # Get the current positions of the trackbars
    h_lower = cv2.getTrackbarPos('Lower Hue', WINDOW_NAME)
    h_upper = cv2.getTrackbarPos('Upper Hue', WINDOW_NAME)
    s_lower = cv2.getTrackbarPos('Lower Saturation', WINDOW_NAME)
    s_upper = cv2.getTrackbarPos('Upper Saturation', WINDOW_NAME)
    v_lower = cv2.getTrackbarPos('Lower Value', WINDOW_NAME)
    v_upper = cv2.getTrackbarPos('Upper Value', WINDOW_NAME)

    # Error handling
    if h_lower < 0 or h_upper < 0:
        break
    if s_lower < 0 or s_upper < 0:
        break
    if v_lower < 0 or v_upper < 0:
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()

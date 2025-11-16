import numpy as np
from tutorial_utils import utils
import cv2

# File path to image used in this tutorial
DATA_DIR = utils.data_dir()

# Create a VideoCapture object.
# Use the filename as the argument.
cap = cv2.VideoCapture(DATA_DIR + "vtest.avi")


# If the capture could not be initialized or some reason, exit
if not cap.isOpened():
    print("Cannot open video file!")


while cap.isOpened():

    # Capture frame-by-frame
    ret, frame = cap.read()


    # If the frame is read correctly, ret == true, and 'frame' contains image data
    # Else ret == false, and we need to exit
    if not ret:
        print("Cannot receive frame (stream end?). Exiting...")
        break

    # Frame is read correctly, so do some operations on it

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', gray)

    # Keep showing the frame for 25ms unless 'q' is pressed
    if cv2.waitKey(25) == ord('q'):
        break

# Release the capture
cap.release()

# Destroy all windows
cv2.destroyAllWindows()
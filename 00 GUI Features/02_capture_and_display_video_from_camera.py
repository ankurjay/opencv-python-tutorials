import numpy as np
import cv2 

# Create a VideoCapture object
cap = cv2.VideoCapture(0)


# If the capture could not be initialized for some reason, exit
if not cap.isOpened():
    print("Cannot open camera!")
    exit()


# Get the properties of the capture using cap.get(prop_id)
default_frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
default_frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

# Default frame width x height = 640 x 480
print("Default Frame Width : %s, Frame Height : %s" % (default_frame_width, default_frame_height))

# Modify the properties using cap.set(prop_id, value)
NEW_FRAME_WIDTH = 1080
NEW_FRAME_HEIGHT = 960

cap.set(cv2.CAP_PROP_FRAME_WIDTH, NEW_FRAME_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, NEW_FRAME_HEIGHT)
print("New Frame Width : %s, Frame Height : %s" % (NEW_FRAME_WIDTH, NEW_FRAME_HEIGHT))


# While the capture is available
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

    # Keep showing the frame for 1ms unless 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture
cap.release()

# Destroy all windows
cv2.destroyAllWindows()
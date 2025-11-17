'''
This file acts as supplementary material for 00_Getting_Started.ipynb
'''

import numpy as np
import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Define the codec
codec = cv2.VideoWriter.fourcc(*'X264')

# Create a VideoWriter object with the codec
out = cv2.VideoWriter('/tmp/output.mkv', codec, fps=20, frameSize=(640, 480))


while cap.isOpened():

    # Capture frame-by-frame
    ret, frame = cap.read()


    # If the frame is read correctly, ret == true, and 'frame' contains image data
    # Else ret == false, and we need to exit
    if not ret:
        print("Cannot receive frame (stream end?). Exiting...")
        break

    # Frame is read correctly, so do some operations on it

    # Flip image upside-down
    frame = cv2.flip(frame, 0)

    # Write the flipped frame to file
    out.write(frame)

    # Also display the flipped frame in a window
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture
cap.release()

# Release the writer
out.release()

# Destroy all windows
cv2.destroyAllWindows()    
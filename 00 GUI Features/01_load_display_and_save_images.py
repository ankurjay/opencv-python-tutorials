'''
This file acts as supplementary material for 00_Getting_Started.ipynb
'''

import sys
from tutorial_utils import utils
import cv2

# File path to image used in this tutorial
DATA_DIR = utils.data_dir()


# Read the image
img = cv2.imread(DATA_DIR + 'starry_night.jpg')

# Check if the image was loaded correctly
if img is None:
    sys.exit("Could not read the image!")
    
print("Image loaded. Displaying...")

# Create a Window
cv2.namedWindow('Starry Night', cv2.WINDOW_AUTOSIZE)

# Display image in the window
cv2.imshow("Starry Night", img)

# Wait for a key press to close the image
k = cv2.waitKey(0)

# If the key pressed was 's', save the iamge
if k == ord('s'):
    cv2.imwrite("/tmp/starry_night_saved.png", img)

# Cleanly destroy window
cv2.destroyWindow("Starry Night")
'''
This file acts as supplementary material for 01_Basic_Operations.ipynb
'''

import numpy as np
import cv2
from tutorial_utils.utils import *

DATA_DIR = data_dir()

cv2.namedWindow('ROI', cv2.WINDOW_NORMAL)

img = cv2.imread(DATA_DIR + "messi5.jpg")

while True:
    cv2.imshow("ROI", img)

    bounds = cv2.selectROI("ROI", img, showCrosshair=True, fromCenter=False)

    print("ROI Bounds : ", bounds)

    # Wait indefinitely for 'q' or Esc Key Press to close window
    k = cv2.waitKey(0) & 0xFF
    if k == ord('q') or k == 27:
        break

cv2.destroyAllWindows()
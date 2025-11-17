import os
from matplotlib import pyplot as plt
import cv2

def data_dir():
    '''
    Returns the path to the 'data' folder
    '''
    return os.path.dirname(os.path.abspath(__file__)) + '/data/'


def cv2_imshow(img, title='default', dpi=100):
    '''
    OpenCV uses BGR, while Matplotlib uses RGB.
    This function takes an OpenCV BGR img and converts it into RGB
    Then it displays the image using matplotlib

    Note: This function expects a BGR or Grayscale image, typically those that 
    are read using cv2.imread(). Often, users may operate on such images, including
    changing the color-space to HSV, YCrCb, RGBA etc. If the colorspace is changed,
    such images will still be plotted by this function but they may not be 
    meaningful, or are upto the interpretation of the user. Images in OpenCV are just 
    numpy arrays containing raw pixel data - the type of color-space is not 
    explicitly encoded in it.
    '''

    # Convert to RGB image
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Get image dimensions
    height, width = rgb_img.shape[:2]

    # Calculate the figure size in inches to preserve actual pixel size at given DPI
    figsize_inches = (width/dpi, height/dpi)

    # Create the figure and axes
    fig, ax = plt.subplots(figsize=figsize_inches, dpi=dpi)

    # Display the image
    ax.imshow(rgb_img)

    # Customize the plot to remove extra space and axes for a clean image
    ax.set_title(title)
    ax.axis('off')
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    
    plt.show()


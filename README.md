# OpenCV Tutorials

This repository contains **Python** scripts that carry out tutorials for various modules in OpenCV. It makes use of both free `(opencv)` and non-free `(opencv_contrib)` packages, and therefore, requires compilation of OpenCV from source. A setup script is provided that handles this compilation and cleanup.

The tutorials are loosely based on https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html

Sample images used in the tutorials come from https://github.com/opencv/opencv/tree/master/samples/data.

## First-Time Installation Guide


> ### Compatibility Warning
> 
> This repository has been tested and is known to work on **Ubuntu 24.04 LTS (Noble Numbat)**. The OpenCV version used is 4.9.0. 
> Since OpenCV is  compiled from source, the resulting compiled libraries are specific to this Linux distribution. They may **not** work on Windows, Mac OS or different Linux distributions.

1. Clone the git repository onto your machine.

```
git clone https://github.com/ankurjay/opencv-python-tutorials.git
```

2. Run the setup script

```
cd <your-target-directory>/opencv-tutorials

chmod +x install.sh

./install.sh
```

3. Wait for the script to finish. This step may take 5-30 minutes depending on your system speed. After compilation is complete, close the terminal.


4. You now have an Isolated Environment that is setup to use OpenCV!

## Using the Isolated Environment

After the initial installation is complete, you need to **activate** the environment.

Open up a new terminal and type:

```
cd <your-target-directory>/opencv-tutorials

source opencv_env/bin/activate.sh
```

You will see `(opencv_env)` appear at the start of your terminal prompt, indicating that your environment is now successfully activated.


## Running a Tutorial

Each tutorial consists of a folder with a `*.ipynb` Jupyter Notebook, and optionally some image/video files that are used in the tutorial. Some tutorials may also have a `*.py` Python script. 

Each `.ipynb` notebook has code interweaved with notes. In the event that a specific functionality of OpenCV needs to be demonstrated using a Python script, instructions for that are provided towards the end of the `.ipynb` notebook.

### Running Jupyter Notebooks

Once you have an activated environment, you can launch a Jupyter Notebook in the `opencv-tutorials` folder like this:

```jupyter notebook```

This will open a browser window in which you can navigate the various directories in this folder, and open the `.ipynb` of your choice directly.
 
> Jupyter Notebooks need some workarounds to work with some OpenCV functions. For example, OpenCV's `cv2.imshow()` opens up a separate GUI window, which isn't supported by Jupyter. So we need to `matplotlib` instead. However, `matplotlib.imshow()` expects images in `RGB` format, while OpenCV loads images in `BGR` format. So we need to apply a conversion, without which, the colors will look off. 
>
> Jupyter Notebooks also don't support real-time playback of video frames. You can show single frames and loop through them. 
>
> To ensure that most of the image processing is done in a format that OpenCV expects, some utility functions have been provided inside `utils/utils.py`, such as `cv_imshow()` that internally uses `matplotlib.pyplot.imshow()` after converting the image from `BGR` to `RGB`.


### Running Python Scripts

Once you have an activated environment, you can run a script normally like this:

```python3 your_script_name.py```


## Cleaning up

If you want to remove the installed environment and binaries (potentially to do a clean install), use the provided `cleanup.sh` script. 

```
cd <your-target-directory>/opencv-tutorials

chmod +x cleanup.sh

./cleanup.sh
```

Now, you can rerun `install.sh` as shown in the **First-Time Installation Guide**, if you want to re-install this project. 

Or, if you want to completely remove this project,

```
cd <your-target-directory>

rm -rf opencv-tutorials
```


## Markdown Preview in VS Code

If you are using VS Code, you can view the rendered markdown files using `Ctrl + Shift + V`
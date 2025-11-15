#!/bin/bash

# Exit immediately if a command fails
set -e


#---------- Define Variables ----------------------
# Name the isolated development environment
ENV_NAME="opencv_env"

# Determine directory location
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
cd "$SCRIPT_DIR"

# Place the compiled OpenCV library in the install directory
INSTALL_DIR="$SCRIPT_DIR/$ENV_NAME"

# Place the OpenCV source code in the opencv_src directory
OPENCV_SRC_DIR="$SCRIPT_DIR/opencv_src"

# Get a stable, recent version of OpenCV
OPENCV_VERSION="4.9.0" # Use a stable, recent version


#---------- Install System Dependencies ----------
sudo apt update
sudo apt install python3 python3-dev python3-pip
sudo apt install -y build-essential cmake git pkg-config libgtk2.0-dev libavcodec-dev libavformat-dev libswscale-dev

#---------- Setup Isolated Python Environment ----
if [ -d "$INSTALL_DIR" ]; then
  echo "Removing existing virtual environment to do a clean install"
  rm -rf "$INSTALL_DIR"
fi
python3 -m venv "$INSTALL_DIR"

echo "Activating Virtual Environment for Building Files"
source "$INSTALL_DIR/bin/activate"

# Ensure numpy is in its latest version
pip install --upgrade numpy

# Install Matplotlib
pip install --upgrade matplotlib

# Install Jupyter Notebook
pip install --upgrade notebook

# Register the opencv_env as a Python kernel that can be used in the Jupyter Notebook
pip install ipykernel
python -m ipykernel install --user --name=opencv_env --display-name "Python (opencv_env)"

# Install local utils package
cd "$SCRIPT_DIR"
pip install -e .


#---------- Download OpenCV Source Code ----------
mkdir -p "$OPENCV_SRC_DIR"
cd "$OPENCV_SRC_DIR"

# Clone main repo
git clone https://github.com/opencv/opencv.git
cd opencv
git checkout $OPENCV_VERSION
cd ..


# Clone contrib repo
git clone https://github.com/opencv/opencv_contrib.git
cd opencv_contrib
git checkout $OPENCV_VERSION
cd ..

# Build and Install OpenCV with Non-Free Modules
cd "$OPENCV_SRC_DIR/opencv"
mkdir -p build
cd build

cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX="$INSTALL_DIR" \
      -D OPENCV_ENABLE_NONFREE=ON \
      -D OPENCV_EXTRA_MODULES_PATH="../../opencv_contrib/modules" \
      -D PYTHON_EXECUTABLE="$INSTALL_DIR/bin/python3" \
      -D INSTALL_PYTHON_EXAMPLES=OFF \
      -D BUILD_EXAMPLES=OFF \
      -D BUILD_opencv_python3=ON \
      ..

make -j$(nproc) # Use all available cores for compilation
make install


# Deactivate the temp environment in the script's subshell
deactivate

# Go back to the script's original directory
# Clean up the OpenCV Source files
cd "$SCRIPT_DIR"
rm -rf "$OPENCV_SRC_DIR"


echo "--- Setup Complete! ---"
echo "To enter your isolated environment and use OpenCV, run the following command in your terminal:"
echo ""
echo "    source \"$INSTALL_DIR/bin/activate\""
echo ""
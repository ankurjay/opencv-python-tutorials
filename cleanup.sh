#!/bin/bash

# Exit immediately if a command fails
set -e

#---------- Define Variables ----------------------
ENV_NAME="opencv_env"
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
INSTALL_DIR="$SCRIPT_DIR/$ENV_NAME"
OPENCV_SRC_DIR="$SCRIPT_DIR/opencv_src"

#---------- Remove Virtual Environment ------------
if [ -d "$INSTALL_DIR" ]; then
  echo "Removing virtual environment at $INSTALL_DIR"
  rm -rf "$INSTALL_DIR"
else
  echo "No virtual environment found at $INSTALL_DIR"
fi

#---------- Remove OpenCV Source Directory --------
if [ -d "$OPENCV_SRC_DIR" ]; then
  echo "Removing OpenCV source directory at $OPENCV_SRC_DIR"
  rm -rf "$OPENCV_SRC_DIR"
else
  echo "No OpenCV source directory found at $OPENCV_SRC_DIR"
fi

#---------- Optional: Uninstall System Dependencies ----------
read -p "Do you want to uninstall the system packages installed during setup? [y/N]: " UNINSTALL
if [[ "$UNINSTALL" =~ ^[Yy]$ ]]; then
  echo "Uninstalling system dependencies..."
  sudo apt remove --purge -y python3-dev python3-pip build-essential cmake git pkg-config libgtk2.0-dev libavcodec-dev libavformat-dev libswscale-dev
  sudo apt autoremove -y
else
  echo "Skipping system package removal."
fi

echo "--- Cleanup Complete! ---"

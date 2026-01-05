# Image Processing Toolkit

This repository contains a collection of tools and scripts for image processing tasks.
It is designed for educational purposes, experiments, and research in image processing.

## Project Structure

### 1. `fft2` - Fast Fourier Transform
This folder contains scripts and tools to explore the effects of **phase** and **magnitude** in images.  
The main functionality involves:
- Applying FFT to two images.
- Manipulating the phase or magnitude of these images.
- Reconstructing and visualizing the effect of these manipulations.

### 2. `conv2` - Convolution Filters
This folder includes tools for creating and applying custom filters to images using convolution operations.  
The main features include:
- Defining custom filters.
- Applying filters to images.
- Visualizing the effects of the filters on the processed images.

### 3. `line_detection` - Line Detection for Robotics
This module implements a computer vision pipeline for detecting lines in images, specifically designed for line follower robots. The algorithm processes images to identify and track lines, calculate positional errors, and provide guidance for robotic navigation.

#### Parameters:
- `THRESHOLD_VALUE`: Controls binary thresholding sensitivity (default: 125)
- `ROI_START: Defines` the starting point of the region of interest as a percentage of image height (default: 0.55)
- `MIN_CONTOUR_AREA`: Minimum area threshold for filtering out small/noisy contours (default: 500)


Document Processing Pipeline

This project provides an automated solution for detecting, cropping, and normalizing scanned documents or photos. It utilizes Computer Vision to transform skewed captures into flat, top-down views and includes a real-time directory monitoring system.
Core Features

    Intelligent Document Detection: Uses OpenCV contour analysis to identify document boundaries within an image.

    Perspective Correction: Implements a four-point perspective transform to normalize camera angles into a 90-degree top-down view.

    Dynamic Scaling: Automatically scales high-resolution images during the detection phase to reduce memory overhead and increase processing speed without sacrificing accuracy.

    Real-time Monitoring: Integrated Watchdog API to monitor a specific folder and programmatically process new images upon creation.

    Automated Rotation: Inference pipeline using ONNX Runtime to detect and correct image orientation (0, 90, 180, 270 degrees).

    Cross-Platform GUI: A user interface built with Flet for managing directory paths, toggling real-time monitoring, and adjusting processing parameters.

Technical Architecture

The system is designed with a modular approach to ensure cross-platform compatibility and performance:

    Frontend (app.py): Flet-based interface for user interaction and directory selection.

    Orchestration (folder_watch.py / crop_rotate_link.py): Manages the flow between file detection, cropping, and orientation correction.

    Vision Engine (autocrop.py): Handles the image processing logic including Gaussian blurring, adaptive thresholding, and perspective warping.

    Inference (predict_onnx.py): Executes the orientation detection model using ONNX Runtime, supporting CUDA, MPS, and CPU execution providers.

Installation

    Clone the repository:
    Bash

    git clone https://github.com/yourusername/project-name.git
    cd project-name

    Install the required dependencies:
    Bash

    pip install opencv-python numpy flet watchdog onnxruntime torch torchvision pillow

Usage
Graphical User Interface

To launch the interactive application:
Bash

python app.py

Command Line Interface

To run the cropping tool independently via CLI:
Bash

python autocrop.py -i /path/to/input -o /path/to/output -t 200 -q 92

Arguments:

    -i: Input path (file or directory).

    -o: Output directory.

    -t: Threshold value for contour detection (default: 200).

    -q: JPEG quality for output images (0-100).

    -p: Number of threads for parallel processing.

Performance Optimizations

    Multiprocessing: Uses Python's multiprocessing.Pool to distribute workloads across available CPU threads, significantly reducing execution time for bulk batches.

    Memory Management: Implements target-area scaling in the contour detection pipeline to prevent high-resolution images from exhausting system RAM.

    Path Handling: Utilizes pathlib for robust file management across Windows, macOS, and Linux.

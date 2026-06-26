# Hand Gesture Volume Control

## Overview

This project uses **MediaPipe** and **OpenCV** to control the system volume through hand gestures. The distance between the **thumb tip** and **index finger tip** is measured and mapped to the system volume level.

## Features

* Real-time hand detection using MediaPipe.
* Tracks 21 hand landmarks.
* Controls system volume using finger distance.
* Displays a visual volume bar and percentage.
* Simple and intuitive gesture-based control.

## Technologies Used

* Python
* OpenCV
* MediaPipe
* NumPy
* Pycaw

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd Gesture-Volume
```

2. Install the required packages:

```bash
pip install opencv-python mediapipe numpy pycaw comtypes
```

## Project Structure

```text
Gesture-Volume/
│
├── main.py          # Main application
├── handDetector.py   # Hand detection module
└── README.md
```

## How It Works

1. Captures video from the webcam.
2. Detects the hand using MediaPipe.
3. Identifies:

   * Thumb Tip (Landmark 4)
   * Index Finger Tip (Landmark 8)
4. Calculates the distance between the two fingertips.
5. Maps the distance to the system volume range.
6. Updates the volume level and displays a volume bar.

## Controls

* Move thumb and index finger closer → Decrease volume.
* Move thumb and index finger farther apart → Increase volume.
* Press **ESC** to exit the application.

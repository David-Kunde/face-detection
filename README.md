Face Detection and Landmark Extraction Script

*Overview*

This script uses OpenCV and MediaPipe libraries to detect faces and extract facial landmarks from a video file.

*Requirements*

- Python 3.x
- OpenCV 4.x
- MediaPipe 0.8.x

*Usage*

1. Install required libraries: `pip install opencv-python mediapipe`
2. Replace `'dave.mp4'` with your video file path.
3. Run the script: `python face_detection.py`

*Functionality*

1. Reads a video file frame by frame.
2. Resizes frames for faster processing.
3. Converts frames to grayscale for optimal face detection.
4. Uses MediaPipe Holistic to detect face landmarks.
5. Draws landmarks on the original frame.
6. Displays the output video feed.

*Controls*

- Press 'q' or 'Q' to quit the script.

*Notes*

- Adjust `min_detection_confidence` and `min_tracking_confidence` for sensitivity.
- For real-time webcam feed, replace `cv2.VideoCapture('dave.mp4')` with `cv2.VideoCapture(0)`.

*Code Structure*

1. Import libraries.
2. Initialize video capture and MediaPipe face mesh.
3. Loop through video frames.
4. Process frames for face detection and landmark extraction.
5. Display output.

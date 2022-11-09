import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture('dave.mp4')
mp_drawing = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh
mp_holistic = mp.solutions.holistic

with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        # getting a frame from video and resizing it
        success, frame = cap.read()
        smaller_frame = cv2.resize(frame, (0, 0), dst=None, fx=0.30, fy=0.30, interpolation=None)

        # changing color of frame to grayscale (best for processing) then processing the grayscale image
        image = cv2.cvtColor(smaller_frame, cv2.COLOR_BGR2RGB)
        results = holistic.process(image).face_landmarks
        print(results)

        image = cv2.cvtColor(smaller_frame, cv2.COLOR_RGB2BGR)
        mp_drawing.draw_landmarks(smaller_frame, results, mp_holistic.FACEMESH_CONTOURS)
        # drawing landmarks on the image
        cv2.imshow('iPhone 6s Live feed', smaller_frame)
        cv2.waitKey(1)
        if cv2.waitKey(10) == (ord('q') | ord('Q')):
            break
cap.release()
cv2.destroyAllWindows()

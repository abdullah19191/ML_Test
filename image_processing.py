import cv2
import numpy as np
import mediapipe as mp
from fastapi.responses import StreamingResponse
from io import BytesIO
from typing import List

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

def process_image(contents: bytes) -> bytes:
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Detect faces in the image
    with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
        results = face_detection.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        
        # Crop the detected faces and draw facial landmarks
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = img.shape
            x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
            mp_drawing.draw_detection(img, detection)

    # Convert the processed image back to bytes
    success, img_encoded = cv2.imencode('.jpg', img)
    img_bytes = img_encoded.tobytes()
    return img_bytes

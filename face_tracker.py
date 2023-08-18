import cv2
import mediapipe as mp
import socket
mp_face_mesh = mp.solutions.face_mesh
cap = cv2.VideoCapture(0)
ClientSocket = socket.socket()
host = '10.0.0.40'
port = 8080
ClientSocket.connect((host, port))
with mp_face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=True, min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:
  while cap.isOpened():
    success, image = cap.read()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(image)
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            ClientSocket.send(str.encode(str(int(results.multi_face_landmarks[0].landmark[0].x * 100)) + "," + str(int(results.multi_face_landmarks[0].landmark[0].y * 100))))
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()

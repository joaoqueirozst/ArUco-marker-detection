import numpy as np
import cv2
import matplotlib.pyplot as plt
from imutils.video import VideoStream
import imutils
import time

# Carrega o dicionario que foi usado para gerar os ArUcos e
# inicializa o detector usando valores padroes para os parametros
parameters =  cv2.aruco.DetectorParameters()
dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_1000)
arucoDetector = cv2.aruco.ArucoDetector(dictionary, parameters)

vs = VideoStream(src=0).start()
time.sleep(2.0)

def load_obj(filename):
    vertices = []
    faces = []
    with open(filename) as file:
        for line in file:
            if line.startswith('v '):
                parts = line.strip().split()
                vertex = [float(parts[1]), float(parts[2]), float(parts[3])]
                vertices.append(vertex)
            elif line.startswith('f'):
                parts = line.strip().split()[1:]
                face = [int(p.split('/')[0]) - 1 for p in parts]
                faces.append(face)
    return np.array(vertices), faces

vertices, faces = load_obj("main/penguin.obj")
vertices = vertices * 0.001 # escala do obj
marker_length = 0.25 # metros

while(True):
    frame = vs.read()
    frame = imutils.resize(frame, width=1024)
    height, width = frame.shape[:2]

    # Matriz de câmera simulada
    focal_length = width
    camera_matrix = np.array([
        [focal_length, 0, width / 2],
        [0, focal_length, height / 2],
        [0, 0, 1]
    ], dtype=np.float64)

    dist_coeffs = np.zeros((5, 1))

    # Detecta os marcadores na imagem
    markerCorners, markerIds, _ = arucoDetector.detectMarkers(frame)
    print(markerCorners)

    if markerIds is not None:
        cv2.aruco.drawDetectedMarkers(frame, corners, ids_m)
        rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(markerCorners, marker_length, camera_matrix, dist_coeffs)

                for rvec, tvec in zip(rvecs, tvecs):
                    
                    # Desenhar eixo de referência no ArUco
                    cv2.drawFrameAxes(frame, camera_matrix, dist_coeffs, rvec, tvec, 0.1)

                    imgpts, _ = cv2.projectPoints(vertices, rvec, tvec, camera_matrix, dist_coeffs)
                    imgpts = imgpts.reshape(-1, 2).astype(int)

                    # Desenha as faces do modelo
                    for face in faces:
                        try:
                            pts = imgpts[face]
                            cv2.polylines(frame, [pts], isClosed=True, color=(0, 0, 0), thickness=1)
                            
                        except IndexError:
                            pass
                            
    cv2.imshow('Aruco_obj',frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()
vs.stop()

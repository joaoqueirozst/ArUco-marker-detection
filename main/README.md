# ArUco Augmented Reality

> Augmented Reality project developed in `Python` using `OpenCV` and `ArUco Markers` for real-time image projection and 3D `.obj` model rendering over markers detected by a camera.
> 
> The system performs marker detection, pose estimation, homography transformation, and 3D object projection, enabling interactive Augmented Reality applications based on computer vision techniques.
> 
> This work was developed in partnership with [Lab. Penguin](https://github.com/Lab-Penguin) and the Intelligent Space ('is'), research laboratories of [IFES](https://guarapari.ifes.edu.br), Guarapari campus.

This repository contains two main approaches:

- Projection of 2D images over detected ArUco markers;
- Projection and animation of 3D `.obj` models in real time.

---

# Features

- Real-time ArUco marker detection;
- Augmented Reality image insertion using homography;
- 3D `.obj` model rendering;
- Pose estimation using `OpenCV`;
- Real-time webcam processing.

---

# Architecture

```bash
main/
├── Penguin.obj
├── requirements.txt
├── aruco_mov.py
└── README.md

src/
├── aruco_img.py
├── img.jpeg # add your image
└── aruco_obj.py
```

This project uses a penguin `.obj` model as the primary 3D object for Augmented Reality simulations, representing a game-like application developed as part of activities presented during the Jornada de Ensino, Pesquisa e Extensão of the campus. However, the system is fully customizable, requiring the user to import the desired `.obj` model and image files according to the intended Augmented Reality tests and applications.

---

# System Requirements

To run the project, you will need:

- Windows, Linux, or MacOS;
- Webcam or USB camera;
- `Python 3` installed;
- `VS Code` (recommended);
- [OpenCV](https://opencv.org/) with ArUco module installed.

---

# requirements.txt

Create a file named:

```bash
requirements.txt
```

Containing:

```txt
opencv-contrib-python
numpy
matplotlib
imutils
```

Install dependencies automatically using:

```bash
pip install -r requirements.txt
```

---

# ArUco Dictionary

The project uses the predefined dictionary:

```python
cv2.aruco.DICT_4X4_1000
```

This dictionary supports up to 1000 unique tags and can be viewed at [ArUco markers generator](https://chev.me/arucogen/).

---

# Camera Input

The webcam stream is initialized using:

```python
VideoStream(src=0).start()
```

If multiple cameras are connected, you may need to change the source index:

```python
VideoStream(src=1).start()
```

---

# Possibilities with ArUco markers

Before presenting the Augmented Reality animation application using sequential ArUco markers, it is important to demonstrate the fundamental capabilities of the system. Initially, the project shows how images and 3D objects can be projected onto ArUco markers in real time, enabling both 2D and 3D Augmented Reality visualization through computer vision techniques, homography transformations, and pose estimation.

## 2D Image Projection

The file:

```bash
image_aruco.py
```

Detects ArUco markers and replaces the marker surface with a custom image using homography transformation. The algorithm performs real-time `ArUco marker` detection by identifying marker regions and extracting their corner coordinates. Using these reference points, the system computes the perspective transformation and applies image warping techniques to project external content directly onto the detected marker surface, enabling real-time `Augmented Reality` visualization.

---

### How to Insert Your Image

Inside the code:

```python
img = cv2.imread('')
```

Replace with your image path:

```python
img = cv2.imread('my_image.png')
```

---

## 3D Object Projection

The file:

```bash
obj_aruco.py
```

The 3D Augmented Reality module loads and renders a `.obj` model directly over detected ArUco markers in real time. The system performs object parsing, vertex transformations, pose estimation, and rotational transformations through rotation matrices, allowing the 3D model to be correctly positioned and oriented according to the marker reference frame. Using `cv2.projectPoints()`, the algorithm projects the 3D coordinates onto the image plane, enabling real-time visualization and rendering of virtual objects integrated into the physical environment.

### 3D Model

The current project uses:

```bash
Penguin.obj
```

You may replace it with another `.obj` model.

---

The project performs pose estimation of the detected ArUco markers using the `cv2.aruco.estimatePoseSingleMarkers()` function. Through this process, the system calculates the rotation vector (`rvec`) and translation vector (`tvec`), allowing the algorithm to determine the spatial position and orientation of each marker relative to the camera reference frame. These parameters are fundamental for correctly aligning virtual objects within the Augmented Reality environment and ensuring consistent 3D projection during real-time visualization.

# Augmented Reality Animation Application

The final application proposed in this project consists of a real-time `Augmented Reality` animation system based on sequential `ArUco marker detection`. The main objective is to position ArUco markers identified by specific `IDs` in an organized spatial arrangement so that they can be detected by the camera and used as reference points for animated 3D object projection.

As the markers are recognized in sequence, the system dynamically projects and animates the `.obj` model over each detected marker, creating the visual perception that the virtual object is moving through a predefined path in the physical environment. The animation logic is implemented through pose estimation, rotational transformations, coordinate displacement, and sequential state transitions between markers.

The movement path, animation behavior, quantity of ArUco markers, and the order of their `IDs` are fully customizable, allowing the development of different trajectories, game simulations, educational activities, and interactive Augmented Reality experiences. At the end of the configured route, the system can display a custom final image, representing the conclusion of the animation or game sequence.

This approach enables the creation of interactive marker-based environments in which virtual objects appear to navigate across the real world using only computer vision techniques and marker tracking.

Main code:

```bash
python3 aruco_mov.py

```

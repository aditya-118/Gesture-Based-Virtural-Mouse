

# Gesture Based Virtual Mouse &nbsp;[![](https://img.shields.io/badge/python-3.8.5-blue.svg)](https://www.python.org/downloads/) [![platform](https://img.shields.io/badge/platform-windows-green.svg)](https://github.com/aditya-118/Gesture-Based-Virtural-Mouse) 

Gesture Controlled Virtual Mouse makes human computer interaction simple by making use of Hand Gestures. The computer requires almost no direct contact. All i/o operations can be virtually controlled by using static and dynamic hand gestures. This project makes use of the state-of-art Machine Learning and Computer Vision algorithms to recognize hand gestures and voice commands, which works smoothly without any additional hardware requirements. It leverages models such as CNN implemented by [MediaPipe](https://github.com/google/mediapipe) running on top of pybind11. It consists of two modules: One which works direct on hands by making use of MediaPipe Hand detection. Currently it works on Windows platform.

Note: Use Python version: 3.8.5

# Features
 _click on dropdown to know more_ <br>

### Gesture Recognition:
<details>
<summary>Neutral Gesture</summary>
 <figure>
  <img src="https://github.com/aditya-118/Gesture-Based-Virtural-Mouse/blob/main/demo_media/Neutral.gif" alt="Palm" width="711" height="400"><br>
  <figcaption>Neutral Gesture. Used to halt/stop execution of current gesture.</figcaption>
</figure>
</details>
 

<details>
<summary>Move Cursor</summary>
  <img src="https://github.com/aditya-118/Gesture-Based-Virtural-Mouse/blob/main/demo_media/Mouse_Movement.gif" alt="Move Cursor" width="711" height="400"><br>
  <figcaption>Cursor is assigned to the midpoint of index and middle fingertips. This gesture moves the cursor to the desired location. Speed of the cursor movement is proportional to the speed of hand.</figcaption>
</details>

<details>
<summary>Right Click</summary>
<img src="https://github.com/aditya-118/Gesture-Based-Virtural-Mouse/blob/main/demo_media/Right_click.gif" alt="Right Click" width="711" height="400"><br>
 <figcaption>Gesture for single right click</figcaption>
</details>

<details>
<summary>Left Click</summary>
<img src="https://github.com/aditya-118/Gesture-Based-Virtural-Mouse/blob/main/demo_media/Left_Click.gif" alt="Left Click" width="711" height="400"><br>
 <figcaption>Gesture for single left click</figcaption>
</details>

<details>
<summary>Scrolling</summary>
<img src="https://github.com/aditya-118/Gesture-Based-Virtural-Mouse/blob/main/demo_media/Scroll.gif" alt="Scrolling" width="711" height="400"><br>
 <figcaption>Dynamic Gestures for horizontal and vertical scroll. The speed of scroll is proportional to the distance moved by pinch gesture from start point. Vertical and Horizontal scrolls are controlled by vertical and horizontal pinch movements respectively.</figcaption>
</details>

<details>
<summary>Drag and Drop</summary>
<img src="https://github.com/aditya-118/Gesture-Based-Virtural-Mouse/blob/main/demo_media/Drag.gif" alt="Drag and Drop" width="711" height="400"><br>
 <figcaption>Gesture for drag and drop functionality. Can be used to move/tranfer files from one directory to other.</figcaption>
</details>


# Getting Started

  ### Pre-requisites
  
  Python: (3.6 - 3.8.5)<br>
  Anaconda Distribution: To download click [here](https://www.anaconda.com/products/individual).
  
  ### Procedure
  ```bash
  git clone https://github.com/xenon-19/Gesture-Controlled-Virtual-Mouse.git
  ```
  For detailed information about cloning visit [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository).
  
  Step 1: 
  ```bash
  conda create --name gest python=3.8.5
  ```
  
  Step 2:
  ```bash
  conda activate gest
  ```
  
  Step 3:
  ```bash
  pip install -r requirements.txt
  ```
  
  Step 5:
  ```bash
 python Gesture_Dataset.py
  ```
 It asks for gesture name and captures the gesture to make dataset.

  Step 6:

  Open the Model_creation.ipynb in Google colab as the code isn't supported in Windows right now and run all the code blocks and download the task file and store in the Model directory. 

  Step 7:
  
  ```bash 
  python Gesture_Controller.py
  ```

# import all the packages necessary
from fileinput import filename

import pyautogui as auto
import cv2 as cv
import numpy as np

# video specifications
# video resolution
resolution = (1920, 1080)

# video codec
codec = cv.VideoWriter_fourcc(*"XVID")

# frames rate of the videos
fps = 60.0

# creating a VideoWriter object (video file)
output = cv.VideoWriter(filename, codec, fps, resolution)

# displaying the recording in real-time

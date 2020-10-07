# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 15:33:53 2020

@author: Poorvahab
"""


import cv2
import numpy as np

bgr = np.uint8([[[56,89,47]]])
hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
print(hsv)
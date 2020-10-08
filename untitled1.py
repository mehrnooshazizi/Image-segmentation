# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 15:33:53 2020

@author: Poorvahab
"""


import cv2
import numpy as np

rgb = np.uint8([[[17,1,126]]])
hsv = cv2.cvtColor(rgb, cv2.COLOR_BGR2HSV)
print(hsv)
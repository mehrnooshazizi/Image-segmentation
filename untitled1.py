# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 15:33:53 2020

@author: Poorvahab
"""


import cv2
import numpy as np

rgb = np.uint8([[[245,149,204]]])
hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)
print(hsv)
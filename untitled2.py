# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 15:42:07 2020

@author: Poorvahab
"""

import numpy as np
import cv2

img1 = cv2.imread('./images/A.jpg');
img2 = cv2.imread('./images/B.png');

r = cv2.bitwise_and(img1,img2)
cv2.imshow('And',r)

r = cv2.bitwise_or(img1,img2)
cv2.imshow('Or',r)

r = cv2.bitwise_xor(img1,img2)
cv2.imshow('Xor',r)

cv2.imshow('Image1',img1)
cv2.imshow('Image2',img2)

r = cv2.bitwise_not(img1)
cv2.imshow('Not',r)

cv2.waitKey(0)

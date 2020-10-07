# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 15:44:13 2020

@author: Azizi
"""

import cv2
#import numpy as np
imgmain = cv2.VideoCapture('G:/New folder/github/Image-segmentation/colored pencils.mp4')
while True:
    _,frame= imgmain.read()
    cv2.imshow('main',frame)
    imgrgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(imgrgb, cv2.COLOR_RGB2HSV)
    print(img)

# light_green = (66 - 10, 120 - 10,  89 - 10)
# dark_green = (66 + 10, 120 + 10,  89 + 10)
# mask_green = cv2.inRange(img, light_green , dark_green)

# light_blue = (105 - 10, 208 - 10,  180 - 10)
# dark_blue = (105 + 10, 208 + 10,  180 + 10)
# mask_blue = cv2.inRange(img, light_blue , dark_blue)

# light_yellow = (24 - 10, 211 - 10,  255 - 10)
# dark_yellow = (24 + 10, 211 + 10,  255 + 10)
# mask_yellow = cv2.inRange(img, light_yellow , dark_yellow)

# light_pink = (163 - 10, 100 - 10,  245 - 10)
# dark_pink = (163 + 10, 100 + 10,  245 + 10)
# mask_pink = cv2.inRange(img, light_pink , dark_pink)

# light_red = (178 - 10, 221 - 10,  224 - 10)
# dark_red = (178 + 10, 221 + 10,  224 + 10)
# mask_red = cv2.inRange(img, light_red, dark_red)

# mask_final = mask_green + mask_blue + mask_yellow + mask_pink + mask_red
# result_final = cv2.bitwise_and(img , img , mask = mask_final)
# result_final = cv2.cvtColor(result_final, cv2.COLOR_HSV2RGB)


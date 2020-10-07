# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 15:44:13 2020

@author: Poorvahab
"""

import cv2
#import numpy as np
import matplotlib.pyplot as plt

imgmain = cv2.imread('G:/New folder/github/Image-segmentation')

imgrgb = cv2.cvtColor(imgmain, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(imgrgb, cv2.COLOR_RGB2HSV)
print(img)

#69 205 177
################################
#light_green = (69 - 10, 205 - 10,  177 - 10)
#dark_green = (69 + 10, 205 + 10,  177 + 10)

#mask_green = cv2.inRange(img, light_green , dark_green)
#result_green = cv2.bitwise_and(img,img, mask = mask_green)
#result_green = cv2.cvtColor(result_green, cv2.COLOR_HSV2RGB)

##179 226 237
#light_red = (179 - 10, 226 - 10,  237 - 10)
#dark_red = (179 + 10, 226 + 10,  237 + 10)
#mask_red = cv2.inRange(img, light_red, dark_red)
#result_red = cv2.bitwise_and(img , img , mask = mask_red)
#result_red = cv2.cvtColor(result_red, cv2.COLOR_HSV2RGB)
######################################
light_green = (69 - 10, 205 - 10,  177 - 10)
dark_green = (69 + 10, 205 + 10,  177 + 10)
mask_green = cv2.inRange(img, light_green , dark_green)

light_red = (179 - 10, 226 - 10,  237 - 10)
dark_red = (179 + 10, 226 + 10,  237 + 10)
mask_red = cv2.inRange(img, light_red, dark_red)

mask_final = mask_green + mask_red
result_final = cv2.bitwise_and(img , img , mask = mask_final)
result_final = cv2.cvtColor(result_final, cv2.COLOR_HSV2RGB)

plt.subplot(3,2,1)
plt.imshow(imgrgb)
plt.subplot(3,2,2)
plt.imshow(mask_green)
print(mask_green)
plt.subplot(3,2,3)
plt.imshow(mask_red)
#plt.subplot(3,2,4)
#plt.imshow(result_green)
plt.subplot(3,2,5)
plt.imshow(result_final)

plt.show()

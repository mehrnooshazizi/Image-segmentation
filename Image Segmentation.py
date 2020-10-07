# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 15:44:13 2020

@author: Azizi
"""

import cv2
#import numpy as np
imgmain = cv2.VideoCapture('G:/New folder/github/Image-segmentation/colored pencils.mp4')
counter=1
while True:
    _,frame= imgmain.read()
    cv2.imshow('main',frame)
    imgrgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(imgrgb, cv2.COLOR_RGB2HSV)
    print(img)

###############################GREEN#####################################
    light_green = (66 - 10, 120 - 10,  89 - 10)
    dark_green = (66 + 10, 120 + 10,  89 + 10)
    mask_green = cv2.inRange(img, light_green , dark_green)
    
    result_green = cv2.bitwise_and(img , img , mask = mask_green)
    result_green = cv2.cvtColor(result_green, cv2.COLOR_HSV2RGB)
    result_green = cv2.resize(result_green,(200,200))
    cv2.imwrite(f'G:/mehrnoosh/green{counter}.jpg',result_green)
    cv2.putText(result_green,str(counter),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
    cv2.imshow('samples',result_green)
    
##############################BLUE########################################
    light_blue = (105 - 10, 208 - 10,  180 - 10)
    dark_blue = (105 + 10, 208 + 10,  180 + 10)
    mask_blue = cv2.inRange(img, light_blue , dark_blue)
    
    result_blue = cv2.bitwise_and(img , img , mask = mask_blue)
    result_blue = cv2.cvtColor(result_blue, cv2.COLOR_HSV2RGB)
    result_blue = cv2.resize(result_blue,(200,200))
    cv2.imwrite(f'G:/mehrnoosh/blue{counter}.jpg',result_blue)
    cv2.putText(result_blue,str(counter),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
    cv2.imshow('samples',result_blue)
#############################YELLOW#######################################    
    light_yellow = (24 - 10, 211 - 10,  255 - 10)
    dark_yellow = (24 + 10, 211 + 10,  255 + 10)
    mask_yellow = cv2.inRange(img, light_yellow , dark_yellow)
    
    result_yellow = cv2.bitwise_and(img , img , mask = mask_yellow)
    result_yellow = cv2.cvtColor(result_yellow, cv2.COLOR_HSV2RGB)
    result_yellow = cv2.resize(result_yellow,(200,200))
    cv2.imwrite(f'G:/mehrnoosh/yellow{counter}.jpg',result_yellow)
    cv2.putText(result_yellow,str(counter),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
    cv2.imshow('samples',result_yellow)
##############################PINK########################################
    light_pink = (163 - 10, 100 - 10,  245 - 10)
    dark_pink = (163 + 10, 100 + 10,  245 + 10)
    mask_pink = cv2.inRange(img, light_pink , dark_pink)
    
    result_pink = cv2.bitwise_and(img , img , mask = mask_pink)
    result_pink = cv2.cvtColor(result_pink, cv2.COLOR_HSV2RGB) 
    result_pink = cv2.resize(result_pink,(200,200))
    cv2.imwrite(f'G:/mehrnoosh/pink{counter}.jpg',result_pink)
    cv2.putText(result_pink,str(counter),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
    cv2.imshow('samples',result_pink)    
###############################RED########################################    
    light_red = (178 - 10, 221 - 10,  224 - 10)
    dark_red = (178 + 10, 221 + 10,  224 + 10)
    mask_red = cv2.inRange(img, light_red, dark_red)
    
    result_red = cv2.bitwise_and(img , img , mask = mask_red)
    result_red = cv2.cvtColor(result_red, cv2.COLOR_HSV2RGB)
    result_red = cv2.resize(result_red,(200,200))
    cv2.imwrite(f'G:/mehrnoosh/red{counter}.jpg',result_red)
    cv2.putText(result_red,str(counter),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
    cv2.imshow('samples',result_red)   
    
    counter+=1
    if( cv2.waitKey(1) == 27):
      break;



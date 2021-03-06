# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 15:44:13 2020

@author: Azizi
"""
import cv2

imgmain = cv2.VideoCapture('G:/New folder/github/Image-segmentation/colored pencils.mp4')
counter=1
while True:
    _,frame= imgmain.read()
    cv2.imshow('main',frame)
    imgrgb = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    img = cv2.cvtColor(imgrgb, cv2.COLOR_RGB2HSV)

###############################GREEN#####################################

    light_green = (50, 160, 110)
    dark_green = (90, 220, 220)
    mask_green = cv2.inRange(img, light_green , dark_green)
    result_green = cv2.bitwise_and(img , img , mask = mask_green)
    result_green = cv2.cvtColor(result_green, cv2.COLOR_HSV2RGB)
    cv2.imwrite(f'G:/mehrnoosh/green{counter}.jpg',result_green)
    cv2.putText(result_green,str(counter),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
    cv2.imshow('green sample',result_green)

##############################BLUE########################################

    light_blue = (125, 50, 50)
    dark_blue = (134, 255, 255)
    mask_blue = cv2.inRange(img, light_blue , dark_blue)    
    result_blue = cv2.bitwise_and(img , img , mask = mask_blue)
    result_blue = cv2.cvtColor(result_blue, cv2.COLOR_HSV2BGR)    
    cv2.imwrite(f'G:/mehrnoosh/blue{counter}.jpg',result_blue)
    cv2.putText(result_blue,str(counter),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
    cv2.imshow('blue sample',result_blue)

#############################YELLOW####################################### 
   
    light_yellow = (95, 50, 50)
    dark_yellow = (105, 255, 255)
    mask_yellow = cv2.inRange(img, light_yellow , dark_yellow)    
    result_yellow = cv2.bitwise_and(img , img , mask = mask_yellow)
    result_yellow = cv2.cvtColor(result_yellow, cv2.COLOR_HSV2RGB)
    cv2.imwrite(f'G:/mehrnoosh/yellow{counter}.jpg',result_yellow)
    cv2.putText(result_yellow,str(counter),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
    cv2.imshow('yellow sample',result_yellow)

##############################PINK########################################

    light_pink = (135, 20, 100)
    dark_pink = (190, 255, 255)
    mask_pink = cv2.inRange(img, light_pink , dark_pink)    
    result_pink = cv2.bitwise_and(img , img , mask = mask_pink)
    result_pink = cv2.cvtColor(result_pink, cv2.COLOR_HSV2RGB) 
    cv2.imwrite(f'G:/mehrnoosh/pink{counter}.jpg',result_pink)
    cv2.putText(result_pink,str(counter),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
    cv2.imshow('pink sample',result_pink)
   
    counter+=1
    if( cv2.waitKey(1) == 27):
      break;



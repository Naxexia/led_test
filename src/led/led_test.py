# coding=UTF-8
'''
Created on 2016年12月10日

@author: dmnnaxxi
'''

import cv2

#read image
img = cv2.imread("E:\\ledpic\\led.bmp")
cv2.imshow('Input image',img)
#cv2.waitKey()

#converter image to gray
img_gray =  cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('GRAY image' , img_gray)


#Extract all the contours from the image
ret,thresh = cv2.threshold(img_gray,210,255,0)
cv2.imshow("Thresh image",thresh)
contours,hierarchy = cv2.findContours(thresh,1,2)
good_contours = []
arc_lengths=[]
for contour in contours:
    if cv2.arcLength(contour,0) > 20:
        cv2.drawContours(img,[contour],-1,(0,0,255),0)
        cv2.imshow('Output',img)
        good_contours.append(contour)
        
cv2.waitKey()
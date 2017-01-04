# coding=UTF-8
'''
Created on 2016年12月10日

@author: dmnnaxxi
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt



#read image
img = cv2.imread("E:\\ledpic\\led.bmp")
#cv2.imshow('Input image',img)
#cv2.waitKey()

#converter image to gray
img_gray =  cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow('GRAY image' , img_gray)

ret,thresh = cv2.threshold(img_gray,175,255,0)
cv2.imshow("Thresh image",thresh)
kernel = np.ones((4,4),np.uint8)
kernel2 = np.ones((3,3),np.uint8)
erosion = cv2.erode(thresh,kernel,1)


#cv2.imshow("erode" ,erosion)
#erosion2 = cv2.morphologyEx(img_gray,cv2.MORPH_OPEN,kernel,2)


#Extract all the contours from the image
#ret,thresh = cv2.threshold(erosion,175,255,0)
#cv2.imshow("Thresh image",thresh)
thresh = cv2.morphologyEx(erosion,cv2.MORPH_ELLIPSE,kernel,2)
#th2 = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,-5)
#th3 = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,-15)

cv2.imshow("morph open",thresh)
#cv2.imshow("Adaptive thresh1 image",th2)
#cv2.imshow("Adaptive thresh2 image",th3)
thresh = cv2.dilate(thresh,kernel2,1)

cv2.imshow("morph close",thresh)

contours,hierarchy = cv2.findContours(thresh,1,2)
good_contours = []
arc_lengths=[]
for contour in contours:
    if cv2.arcLength(contour,0) > 0:
        cv2.drawContours(img,[contour],-1,(0,0,255),0)
        cv2.imshow('Output',img)
        good_contours.append(contour)       
cv2.waitKey()
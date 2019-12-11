#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def detectCells(img):
    import cv2 as cv
    import numpy as np        
    from math import pi, pow
    cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
    circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,15,
                                param1=100,param2=20,minRadius=10,maxRadius=35)
    circles = np.uint16(np.around(circles))
    area = []
    for i in circles[0,:]:
        # draw the outer circle
        cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
        area.append(pow(i[2],2) * pi)
    return (cimg,circles, area)
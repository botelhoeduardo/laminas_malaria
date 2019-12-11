import cv2 as cv,cv2
import numpy as np
import matplotlib
import scipy
from matplotlib import pyplot as plt
matplotlib.use('TkAgg')
img = cv.imread('IMG-20180701-WA0030.jpg',0)
img = cv.medianBlur(img,5)
#filtro passa alta laplace(erro)
#img = cv.Laplacian(img,cv.CV_64F)

#filtro passa-alta
#kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
#img = cv.filter2D(img, -1, kernel)

cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,2,20,
                            param1=50,param2=30,minRadius=0,maxRadius=10)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
# draw the outer circle
  cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
# draw the center of the circle
  #cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

  cv2.imshow('detected circles',cimg)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
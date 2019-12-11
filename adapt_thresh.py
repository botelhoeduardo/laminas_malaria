import cv2 as cv
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from extrair_fundo import extrairfundo
from equalization import equalizar
from detect_cells import detectCells
matplotlib.use('TkAgg')
img = cv.imread('IMG-20180701-WA0031.jpg',0)
img = cv.medianBlur(img,5)
img = extrairfundo(img)
imgeq = equalizar(img,2.0)

th3 = cv.adaptiveThreshold(imgeq,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,11,2)
#_, th3 = cv.threshold(imgeq,50,255,cv.THRESH_BINARY)
#inverter imagem
th3 = (255-th3)

ellipsis = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,5))
square = np.ones((5,5),np.uint8)
th4 = cv.erode(th3, ellipsis, iterations=1)
th4 = cv.GaussianBlur(th4,(3,3),0)

output = img.copy()
output = cv.cvtColor(output,cv.COLOR_GRAY2RGB)
output[th4 == 255] = [255, 0, 0]

(cimg, circles, area) = detectCells(imgeq)

area_plasm = np.sum(th4[th4 == 255])/255
area_cells = np.sum(area)
area_inf = (100 * area_plasm) / area_cells

print('{0:.2f}% das células infectadas'.format(area_inf))

titles = [
    'Original Equalizada', 'Supostas aglomerações de plasmodium', 'Hough Circles']
images = [imgeq, output, cimg]

for i in range(3):
    plt.subplot(1,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
while True:
    if plt.waitforbuttonpress():
        break
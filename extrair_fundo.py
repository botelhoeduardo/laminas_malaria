def extrairfundo(img):
    import cv2 as cv
    import numpy as np

    if img.ndim == 3:
        IR = img[:,:,0]
        IG = img[:,:,1]
        IB = img[:,:,2]

        ret,th1 = cv.threshold(IR,50,255,cv.THRESH_BINARY)
        ret,th2 = cv.threshold(IG,50,255,cv.THRESH_BINARY)
        ret,th3 = cv.threshold(IB,50,255,cv.THRESH_BINARY)

        IR = np.multiply((255-IR),th1)
        IG = np.multiply((255-IG),th2)
        IB = np.multiply((255-IB),th3)

        semfundo = np.dstack((IR,IG,IB))
    else:
        ret,th1 = cv.threshold(img,50,255,cv.THRESH_BINARY)

        semfundo = np.multiply((255-img),th1)
        semfundo[th1 == 0] = [255]
    return semfundo
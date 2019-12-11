def equalizar(img,lim):
    import cv2
    clahe = cv2.createCLAHE(clipLimit=lim)
    res = clahe.apply(img)
    return res
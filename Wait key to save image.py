import cv2 as cv
import numpy as np

img=cv.imread('a.jpg')
img1=cv.imread('c.jpg',0)
cv.imshow('image',img)
key=cv.waitKey(0)

if key==27:
    cv.destroyAllWindows()
elif key == ord('q'):
    cv.imshow('image1',img1)
    cv.waitKey(10000)

import cv2 as cv
import numpy as np

img=cv.imread('a.jpg',0)
img1=cv.imread('b.jpg')
cv.imshow('image',img)
cv.imshow('image1',img1)
cv.waitKey(0)
cv.destroyAllWindows()

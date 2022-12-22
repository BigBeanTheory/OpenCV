import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img=cv.imread('sudoku.png',0)
img=cv.medianBlur(img,5)
cv.imshow('Original Image',img)

ret,th1=cv.threshold(img,127,255,cv.THRESH_BINARY)
cv.imshow('Thresholded',th1)

th2=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
th3=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
cv.imshow('Gaussian Thresholding',th3)
cv.imshow('Adaptive Thresholding',th2)

img1=cv.cvtColor(img,cv.COLOR_GRAY2RGB)
img2=cv.cvtColor(th1,cv.COLOR_GRAY2RGB)
img3=cv.cvtColor(th2,cv.COLOR_GRAY2RGB)
img4=cv.cvtColor(th3,cv.COLOR_GRAY2RGB)

plt.subplot(141)
plt.imshow(img1)
plt.subplot(142)
plt.imshow(img2)
plt.subplot(143)
plt.imshow(img3)
plt.subplot(144)
plt.imshow(img4)
plt.show()

cv.waitKey(0)
cv.destroyAlllWindows()

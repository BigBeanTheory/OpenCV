import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img=cv.imread('hazard10.jpeg')

b,g,r=cv.split(img)

#cv.imshow('BLUE',b)
#cv.imshow('GREEN',g)
#cv.imshow('RED',r)

img_merged=cv.merge([b,g,r])
cv.imshow('Photo',img_merged)
plt.subplot(141)
plt.imshow(img)
plt.subplot(142)
plt.imshow(b)
plt.subplot(143)
plt.imshow(g)
plt.subplot(144)
plt.imshow(r)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()

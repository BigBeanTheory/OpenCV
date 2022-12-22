import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img=cv.imread('hazard10.jpeg')
cv.imshow('IMAGE',img)

#finding region of interest
#img_RGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)
#plt.axis('off')
#plt.imshow(img_RGB)
#plt.show()

#Accessing the ball region and converting to white
#ball=img[235:295,465:530]
#ball=([255,255,255])
#img[235:295,465:530]=ball

#Duplicate the ball
ball=img[235:295,465:530]
img[235:295,555:620]=ball

cv.imshow('IMAGE WITH TWO BALLS',img)

cv.waitKey(0)
cv.destroyAllWindows()

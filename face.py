import cv2 as cv
import numpy as np

img=np.zeros((500,500,3),np.uint8)

cv.circle(img,(250,250),150,(255,255,255),5) #outer face

cv.line(img,(175,200),(235,200),(255,255,255),3) #Eyebrows
cv.line(img,(255,200),(315,200),(255,255,255),3)

cv.circle(img,(205,225),20,(255,255,255),-1) #Eye 1
cv.circle(img,(205,225),10,(240,211,102),-1)
cv.circle(img,(205,225),5,(0,0,0),-1)

cv.circle(img,(285,225),20,(255,255,255),-1) #Eye 2
cv.circle(img,(285,225),10,(240,211,102),-1)
cv.circle(img,(285,225),5,(0,0,0),-1)

cv.rectangle(img,(235,230),(250,270),(58,89,255),-1) #Nose

cv.rectangle(img,(200,290),(290,310),(51,1,231),-1) #Mouth
cv.rectangle(img,(210,295),(280,305),(255,255,255),-1)

cv.imshow('Image',img)
cv.waitKey(0)
cv.destroyAllWindows

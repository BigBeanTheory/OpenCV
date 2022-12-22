import cv2 as cv
import numpy as np

img=cv.imread('pic1.png')

img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,thresh=cv.threshold(img_gray,127,255,0)

contours,hierachy=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
cnt=contours[6]
cv.drawContours(img,[cnt],0,(255,0,255),3)

M=cv.moments(cnt) #gives dictionary of all moment values
print(M)

cx=int(M['m10']/M['m00'])
cy=int(M['m01']/M['m00'])

print('Centroid',(cx,cy))

area=cv.contourArea(cnt)
print('Area of the Face is',area)

perimeter=cv.arcLength(cnt,True)
print('Perimeter of the face is',perimeter)

x,y,w,h=cv.boundingRect(cnt)
cv.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)

(x,y),radius=cv.minEnclosingCircle(cnt)
centre=(int(x),int(y))
radius=int(radius)
cv.circle(img,centre,radius,(255,0,0),2)

cv.imshow('Contours',img)

cv.waitKey(0)
cv.destroyAllWindows()

import cv2 as cv
import numpy as np

#creating black background image
img=np.zeros((500,500,3),np.uint8)

#creating a purple line
cv.line(img,(20,20),(500,500),(255,0,255),8)

#creating a rectangle
cv.rectangle(img,(20,20),(480,400),(255,255,0),7)

#creating a circle
cv.circle(img,(250,250),50,(25,130,249),-1)


#writing text in image
font=cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'Nithin is great',(220,250),font,5,(255,0,0),2)

cv.imshow('Image',img)
cv.waitKey(0)
cv.destroyAllWindows()

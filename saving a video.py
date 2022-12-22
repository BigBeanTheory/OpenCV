import cv2 as cv
import numpy as np

cam=cv.VideoCapture(0)

#Define Codec
fourcc=cv.VideoWriter_fourcc(*'XVID')
output=cv.VideoWriter('Output1.avi',fourcc,20.0,(640,480))

while(cam.isOpened()):
    ret,frame=cam.read()
    if ret==True:
        cv.imshow('frame',frame)
        output.write(frame)

        if cv.waitKey(1)==ord('q'):
            print('Saved Video')
            break

    else:
        print('Error in capturin video')
        break

#Release everything

cam.release()
output.release()
cv.destroyAllWindows()

import cv2 as cv
import numpy as np

img=cv.imread('air.jpg')
img=cv.resize(img,dsize=(0,0),fx=3,fy=3) 
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY) 
cv.putText(gray,'air',(10,20),cv.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)

gaussian=np.hstack((cv.GaussianBlur(gray,(5,5),0.0),cv.GaussianBlur(gray,(9,9),0.0),cv.GaussianBlur(gray,(15,15),0.0)))
median = np.hstack((cv.medianBlur(gray, 5), cv.medianBlur(gray, 9), cv.medianBlur(gray, 15)))
cv.imshow('frame',gaussian)
cv.imshow('happy',median)

cv.waitKey() 
cv.destroyAllWindows()
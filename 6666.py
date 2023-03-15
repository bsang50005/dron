import cv2 as cv
import sys
img=cv.imread('happy.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다')
    
cv.rectangle(img,(300,40),(400,190),(0,0,255),2)
cv.arrowedLine(img,(250,50),(300,100),(0,200,10),2)
cv.putText(img,'laugh',(160,40),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

cv.imshow('Draw',img)

cv.waitKey()
cv.destroAllWindows()
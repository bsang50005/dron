import cv2 as cv
import sys

cap=cv.VideoCapture(0,cv.CAP_DSHOW)
gray=False
if not cap.isOpened():
    sys.exit('카메라 연결 실패')
    
    
frames=[] 
while True:
    ret,frame=cap.read()
    
    if not ret:
        print('프레임 획득에 실패하여 루프를 나갑니다')
        break
    if gray:
        frame=cv.cvtColor(cap, cv.COLOR_BGR2GRAY)
    cv.imshow('Video display',frame)
    
    key=cv.waitKey(1)
    
    if key==ord('c'):
        gray=False
    elif key==ord('g'):
        gray=True
    elif key==ord('q'):
        break
cap.release()
cv.destroyAllWindows()
import cv2 as cv
import sys

img = cv.imread('happy.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

def draw(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.rectangle(img, (x,y), (x+20, y+20), (0, 0, 255), 2)
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img, (x,y), 50, (255, 0, 0), 2)
    cv.imshow('Drawing', img)

cv.namedWindow('Drawing')
cv.imshow('Drawing', img)

cv.setMouseCallback('Drawing', draw)

while(True):
    if cv.waitKey(1) == ord('q'):        
        cv.destroyAllWindows()
        break
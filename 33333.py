import cv2 as cv
import sys

img=cv.imread('soccer.jpg' )


if img is None:
    sys.exit('파일을 찾을수 없음')
cv.imwrite('image Display1.png', img)
cv.imshow('img1', img)

img=cv.imread('soccer1.jpg' )


if img is None:
    sys.exit('파일을 찾을수 없음')

cv.imwrite('image Display2.png', img)
cv.imshow('img2', img)

cv.waitKey()
cv.destroyAllWindows()
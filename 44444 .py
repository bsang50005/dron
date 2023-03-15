import cv2 as cv
import sys

img=cv.imread('soccer1.jpg' )


if img is None:
    sys.exit('파일을 찾을수 없음')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray_small=cv.resize(gray,dsize=(0,0),fx=0.1, fy=0.1)
gray_small=cv.resize(gray,dsize=(0,0),fx=0.2, fy=0.2)

cv.imwrite('soccer1_gray.jpg',gray)
cv.imwrite('soccer1_gray_small.jpg',gray_small)


cv.imshow('Color image small',img)
cv.imshow('Gray image small1',gray_small)
cv.imshow('Gray image small2',gray_small)
cv.imshow('Gray image small3',gray_small)
cv.imshow('Gray image small4',gray_small)
cv.imshow('Gray image small5',gray_small)
cv.imshow('Gray image small6',gray_small)
cv.imshow('Gray image small7',gray_small)
cv.imshow('Gray image small8',gray_small)
cv.imshow('Gray image small9',gray_small)



cv.waitKey()
cv.destroyAllWindows()
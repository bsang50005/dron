import time
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread('air.jpg')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
plt.imshow(gray,cmap='gray'),plt.xticks([]),plt.yticks([]),plt.show()

cv.imwrite('gray.jpg',gray)

h=cv.calcHist([gray],[0],None,[256],[0,256])
plt.plot(h,color='r',linewidth=1),plt.show()

equal=cv.equalizeHist(gray)
plt.imshow(equal,cmap='gray'),plt.xticks([]),plt.yticks([]),plt.show()

cv.imwrite('equals.jpg',equal)

h=cv.calcHist([equal],[0],None,[256],[0,256])
plt.plot(h,color='r',linewidth=1),plt.show()

def my_cvtGray1(bgr_img):
    g=np.zeros([bgr_img.shape[0],bgr_img.shape[1]])
    for r in range(bgr_img.shape[0]):
        for c in range(bgr_img.shape[1]):
            g[r,c]=0.144*bgr_img[r,c,0]+0.587*bgr_img[r,c,1]+0.299*bgr_img[r,c,2]
    return np.uint8(g)

def my_cvtGray2(bgr_img):
    g=np.zeros([bgr_img.shape[0],bgr_img.shape[1]])
    g=0.144*bgr_img[:,:,0]+0.587*bgr_img[:,:,1]+0.299*bgr_img[:,:,2]
    return np.uint8(g)

img=cv.imread('soccer.jpg')
img1=cv.imread('gray.jpg')
img2=cv.imread('equals.jpg')

start=time.time()
my_cvtGray1(img1)
print('My time1:',time.time()-start)

start=time.time()
my_cvtGray2(img2)
print('My time2:', time.time()-start)

start=time.time()
cv.cvtColor(img,cv.COLOR_BGR2GRAY)
print('OpenCV time:',time.time()-start)
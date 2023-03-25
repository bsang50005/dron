import cv2 as cv

# callback function for mouse event
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, img, original_img
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            img = original_img.copy()
            cv.rectangle(img, (ix, iy), (x, y), (255, 0, 0), 3)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        cv.rectangle(img, (ix, iy), (x, y), (255, 0, 0), 3)
        patch = original_img[iy:y, ix:x, :]
        patch1 = cv.resize(patch, dsize=(0, 0), fx=5, fy=5, interpolation=cv.INTER_NEAREST)
        patch2 = cv.resize(patch, dsize=(0, 0), fx=5, fy=5, interpolation=cv.INTER_LINEAR)
        patch3 = cv.resize(patch, dsize=(0, 0), fx=5, fy=5, interpolation=cv.INTER_CUBIC)
        cv.imshow('Patch nearest', patch1)
        cv.imshow('Patch bilinear', patch2)
        cv.imshow('Patch bicubic', patch3)

# create window and set mouse callback function
cv.namedWindow('Image')
cv.setMouseCallback('Image', draw_rectangle)

img = cv.imread('rose.png')
original_img = img.copy()

drawing = False
ix, iy = -1, -1

while True:
    cv.imshow('Image', img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()
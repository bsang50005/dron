import cv2 as cv 
import numpy as np

img=cv.imread('soccer.jpg')	# 사커.jpg를 파일에서 읽어와  출력
img_show=np.copy(img)		# 붓 칠을 디스플레이할 목적의 영상

mask=np.zeros((img.shape[0],img.shape[1]),np.uint8) 
mask[:,:]=cv.GC_PR_BGD		# 모든 화소를 배경일 것 같음으로 초기화

BrushSiz=9	# 붓의 크기
LColor,RColor=(255,0,0),(0,0,255) #왼쪽색깔의 크기 오른쪽색깔의 크기

def painting(event,x,y,flags,param): #이미지에 대한 마우스 이벤트 처리함수
    if event==cv.EVENT_LBUTTONDOWN: #마우스 왼쪽버튼을 눌렀을때 발생하는 이벤트는 
        cv.circle(img_show,(x,y),BrushSiz,LColor,-1)# 왼쪽 버튼 클릭하면 파란색
        cv.circle(mask,(x,y),BrushSiz,cv.GC_FGD,-1) #이미지에 마스크를 만들기
    elif event==cv.EVENT_RBUTTONDOWN: #마우스 오른쪽 버튼을 눌렀을때 발생하는 이벤트는
        cv.circle(img_show,(x,y),BrushSiz,RColor,-1) # 오른쪽 버튼 클릭하면 빨간색
        cv.circle(mask,(x,y),BrushSiz,cv.GC_BGD,-1) 
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_LBUTTON:
        #마우스를 이동하면서 왼쪽 버튼이 눌린 상태라면
        cv.circle(img_show,(x,y),BrushSiz,LColor,-1)# 왼쪽 버튼 클릭하면서 이동하면 파란색
        cv.circle(mask,(x,y),BrushSiz,cv.GC_FGD,-1)
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_RBUTTON: 
        #마우스를 이동하면서 오른쪽 버튼이 눌린 상태라면
        cv.circle(img_show,(x,y),BrushSiz,RColor,-1)	# 오른쪽 버튼 클릭하면서 이동하면 빨간색
        cv.circle(mask,(x,y),BrushSiz,cv.GC_BGD,-1)

    cv.imshow('Painting',img_show) #이미지 쇼를 이미지를 페인팅이라는 창에 출력
    
cv.namedWindow('Painting') #페인팅이라는 이름의 창을 생성
cv.setMouseCallback('Painting',painting) 

while(True):				# 조건문이 참일시 
    if cv.waitKey(1)==ord('q'): #q버튼을 누르면 1초의 딜레이를 가지고 끝냄
        break

# 여기부터 GrabCut 적용하는 코드
background=np.zeros((1,65),np.float64)	# 배경 히스토그램 0으로 초기화
foreground=np.zeros((1,65),np.float64)	# 물체 히스토그램 0으로 초기화

cv.grabCut(img,mask,None,background,foreground,5,cv.GC_INIT_WITH_MASK)
#GrabCut은 영상에서 관심 객체를 추출하기 위해 사용되며, 입력 이미지와 함께 초기 마스크
#(관심 객체가 포함된 영역이 표시된 이진 이미지)를 입력으로 받아, 관심 객체에 해당하는 
#영역을 추출
#그랩컷 이라는 함수를 사용하여 이미지에 백그라운드 그리고 포그라g운드 분할 작업 수행
# 백그라운드 배경 포그라운드는 객체
mask2=np.where((mask==cv.GC_BGD)|(mask==cv.GC_PR_BGD),0,1).astype('uint8')
#마스크를 수정하는 작업 수행
grab=img*mask2[:,:,np.newaxis] 
# 마크2는 그랩컷 알고리즘이 적용된 이진 마스크 이미지이고
#마스크의 배경과 물체를 구분하여 배경과 물체가 각각 0과1의 값을 가지도록 설정
#이미지와 같은 크기의 새로운 3차원 배열을 만들어 마크2 값을 3차원 축에 차가하여
#3차원 이미지로 만들어줌 그렇게 만들어진 3차원 이미지와 원래의 이미지를 곱해주면
#배경은 검은색으로 처리되어 사라지고 물체 부분만 남겨진 이미지가 생성
#그를 그랩b라는 변수에 저장
cv.imshow('Grab cut image',grab) #윈도우 창에 그랩b를 그랩컽이미지 창에 출력

cv.waitKey()
cv.destroyAllWindows()
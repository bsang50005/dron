import numpy as np
import matplotlib.pyplot as plt

# 가우시안 함수 정의
def gaussian(x, mu, sigma):
    return np.exp(-((x-mu)/sigma)**2/2) / (sigma * np.sqrt(2*np.pi))

# x 값 범위 설정
x = np.linspace(-5, 5, 100)

# mu와 sigma 설정
mu = 0
sigma = 1

# 가우시안 함수 계산
y = gaussian(x, mu, sigma)

# 그래프 그리기
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('1D Gaussian Function')
plt.show()
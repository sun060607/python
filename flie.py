#시각화 모듈
import matplotlib.pyplot as plt
#부산 3월 기온
temp = [10.8, 8.5, 8.7, 7.9, 5.1, 
        8.1, 8.2, 10.4, 11, 9.9, 
        7.8, 9.5, 11.6, 8.2, 7.7, 
        6.6, 11.1, 12.2, 12.6, 10.4, 
        13.7, 14.1, 12.6, 11.5, 13, 
        14.5, 13.7, 9.4, 10.4, 11.6, 12.9]
!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf
#그래프 그리기
plt.plot(temp)
plt.show()
#STEP 3. matplotlib의 폰트를 Nanum 폰트로 지정
plt.rc('font', family='NanumBarunGothic')
#제목 달기
plt.title('3월 기온')
plt.plot(temp)
plt.show()

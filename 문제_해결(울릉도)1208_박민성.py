# -*- coding: utf-8 -*-
"""문제 해결(울릉도)1208 박민.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jhhU-rQCs3MinP2Ux6rHx-vrvTifafTE
"""

from google.colab import files
file_uploaded = files.upload()

from google.colab import drive
drive.mount('/content/gdrive/')

!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf

import matplotlib.pyplot as plt
plt.rc('fount',family='NanumBarunGothic')

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mat

#파일 읽기
df = pd.read_csv('weather.csv',encoding = 'CP949')
df

#전체 행과 열, 속성 파악
df.shape

df.head()

df.info()

#데이터프레임 통계, 문자 빼고고
df.describe()

#결속치 구하기
df.isnull().sum()
#df['최대 풍속속'].isnull().sum()

#평균풍속 최소값
print("평균풍속의 최소값은은",df['평균풍속'].min(),"m/s입니다다")

#결속치 제거
df2 = df.dropna(how = 'any')
df2.info()

#가장 무더웠던 닐 !!!
hot = df2['평균기온'].max()
hot

hotday = df2['일시'][df2['평균기온'] == hot]
hotday
#1103에 들어있어 그냥 배열로 생각해 1103을 호출출
type(hotday)

print("가장 더운 날짜는",hot,"도",hotday[1103],"입니다")

hotday2 = str(hotday)
hotday2
hotday2 = hotday2[8:18]
print(hotday2)

hottest = df2.loc[df2['평균기온'] == hot]
print("가장 무더웠던 날")
print("="*50)
hottest

#문제 2

hottest = df2.loc[df2['평균기온'] >= 30]
print("가장 무더웠던 날")
print("="*50)
hottest

#문제3

#월 자르기
df2['일시'].str[5:7]
#일 자르기기
df2['일시'].str[8:]

df2['월'] = df2['일시'].str[5:7]
df2

#월 별로 묶기
re = df2.groupby('월')['평균풍속'].mean()

type(re)

re.max()

#re2 = re.index[re == re.max()]
#re
re2 = re.index[re == re.max()].tolist()
print("울릉도는",re2[0],"월에 가장 바람이 강합니다다")

# X ; 월
#Y : 일
#막대그래프 출력, 자료구조 변화 !
y = re.tolist()
x = re.index.tolist()
plt.title('울릉도 월별 풍속')
plt.bar(x, y)
for i in range(0,len(x)):
  if y[i] == max(y):
    plt.text(i,y[i],round(y[i], 1), ha='center',color='g')    # verticalalignment (top, center, bottom)
  else:
    plt.text(i,y[i],round(y[i], 1), ha='center',color='r')
plt.show()
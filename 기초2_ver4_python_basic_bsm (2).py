# -*- coding: utf-8 -*-
"""기초2.ver4_python_basic_bsm.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G1Y00rE1YAqw-B3HJ9Hj9eUgv5ginM23
"""

#해결 문제1
#set으로 출입 명부 만들기
vip_names = ['Newton','Kepler','Euler','Galileo']
room1_list = ['Newton']
room2_list = ['Euler','Galileo']
room1_list=set(room1_list)
room2_list=set(room2_list)
vip_names = set(vip_names)
print(room1_list)
print(room2_list)
print(vip_names - (room1_list|room2_list))

#집합 연산
a = (1,2,2,3,10,20)#튜플
b = [2,10,20,30,30]#리스트

a = set(a)
b = set(b)

print(f"{a} , {b}")
print(f"{a&b}")
print(f"{a | b}")
print(f"{a - b}")
print(f"{b -a}")

#컬렉션 요소 접근
lst = [10,50,30]
tp = ('a','b','c')
for item in lst:
  print(item,end='')
for item in tp:
  print(item, end='')

# 딕셔너리 만들기 : dict() 함수와 zip() 함수 이용
dy = dict(zip(tp,lst))
print(dy)
for item in dy:
  print(f'{item}:{dy[item]}')

"""#내장 함수


*   len(컬렉션명) : 컬렉션 요소 개수
*   max(컬렉션명) : 가장 큰 요소값 반환
    + 딕셔너리인 경우는 키 값 중 가장 큰 요소로 반환
*   min(컬렉션명) : 가장 작은 요소값 반환
    + 딕셔너리인 경우는 키 값 중 가장 작은 요소 반환
*   sum(컬렉션명) : 수치 요소로 이루어진 컬렉션 요소의 합
    + 딕셔너리인 경우는 키 값의 합
*   sorted(컬렉션명) : 컬렉션 요소 정렬
    + 딕셔너리인 경우는 키 값을 정렬하여 키 리스트 반환


"""

# 내장함수
lst = [10,50,30]
print(len(lst))
print(max(lst))

print(min(lst))
print(sum(lst))
print(sorted(lst))
lst.sort()# 안이 바뀜

temp =[10.8, 8.5, 8.7, 7.9, 5.1,
       8.1,8.2,10.4,11,9.9,
       7.8,9.5,11.6,8.2,7.7,
       6.6,11.1,12.2,10.4,
       13.7,14.1,12.6,11.5,13,
       14.5,13.7,9.4,10.4,11.6,12.9
       ]
print(max(temp))
print(min(temp))
print(f'{sum(temp)/len(temp):0.2f}')

y = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
yavg = [14.9,14.6,14.5,15.3,15.1,15.4,15.7,15.2,15.1,15.7]
ymax = [34.1, 33,34.5,35,32.9,33.5,37.3,36.2,36.4,35]
ymin = [19,18.8,18.6,19.5,19.2,19.5,19.8,19.6,19.2,19.8]
for i in y:
  if i%2==1:
    print(i, end=' ')
print()
ytemp=dict(zip(y,yavg))
print(ytemp)

mintemp=min(ytemp.values())
ryear=[]
for year,temp in ytemp.items():
  if temp==mintemp:
    ryear.append(year)
print(f'{ryear}:{mintemp}')

maxv=max(ymax)
ylist=[]
for i in range(len(ymax)):
  if ymax[i]==maxv:
    ylist.append(y[i])
print(f'{ylist}:{maxv}')
ymlist=[]
minv = min(ymin)
for i in range(len(ymin)):
  if ymin[i] == minv:
    ymlist.append(y[i])
print(f'{ymlist}:{minv}')

from google.colab import drive
drive.mount('/content/drive')

# csv 파일 불러오기
filename = '/content/drive/MyDrive/부산.csv'

import csv
f = open(filename, 'r',encoding='cp949')
data = csv.reader(f,delimiter=',')
print(data)
f.close()

# csv 파일 불러오기
filename = '/content/drive/MyDrive/부산.csv'

import csv
f = open(filename, 'r',encoding='cp949')
data = csv.reader(f,delimiter=',')
print(data)
for row in data:
  print(row)
f.close()

# csv 파일 불러오기
filename = '/content/drive/MyDrive/부산.csv'

import csv
f = open(filename, 'r',encoding='cp949')
data = csv.reader(f,delimiter=',')
header = next(data)
for row in data:
  print(row)
f.close()

"""#3. 부산이 가장 더웠던 날은 언제였을까?

  1. 질문 다듬기<BR>
*부산이 가장 더웠던 날은 언제였을까?*<br>
*얼마나 더웠을까*<br>
"""

# csv 파일 불러오기
filename = '/content/drive/MyDrive/부산.csv'

import csv
f = open(filename, 'r',encoding='cp949')
data = csv.reader(f,delimiter=',')
header = next(data)
for row in data:
  print(row[2])
f.close()

# csv 파일 불러오기
filename = '/content/drive/MyDrive/부산.csv'

import csv
f = open(filename, 'r',encoding='cp949')
data = csv.reader(f,delimiter=',')
header = next(data)
for row in data:
  if row[2] == '':
    row[2] == -999
  print(row[2])
f.close()

# csv 파일 불러오기
filename = '/content/drive/MyDrive/부산.csv'
import csv
f = open(filename, 'r',encoding='cp949')
data = csv.reader(f,delimiter=',')
header = next(data)
max_temp = -999
max_date = ''
for row in data:
  if row[2] == '':
    row[2] == -999
  row[2] = float(row[2])
  if max_temp<row[2]:
    max_date = row[0]
    max_temp = row[2]

f.close()
print(max_date,max_temp)

# csv 파일 불러오기
filename = '/content/drive/MyDrive/부산.csv'
import csv
f = open(filename, 'r',encoding='cp949')
data = csv.reader(f,delimiter=',')
header = next(data)
min_temp = 999
min_date = ''
for row in data:
  if row[4] == '':
    row[4] = 999
  row[4] = float(row[4])
  if min_temp > row[4]:
    min_date = row[0]
    min_temp = row[4]

f.close()
print(min_date,min_temp)

import matplotlib.pyplot as plt
plt.plot([10,20,30,40])
plt.show()

import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[12,43,25,15])
plt.show()

!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf

import matplotlib.pyplot as plt
plt.rc('font', family="NanumBarunGothic")
plt.rcParams['axes.unicode_minus'] = False

import matplotlib.pyplot as plt
plt.title('플로팅')
plt.plot([10,20,30,40])
plt.show()

import matplotlib.pyplot as plt
plt.title('범례 넣기기')
plt.plot([10,20,30,40],label = '증가')
plt.plot([40,30,20,10],label = '감소')
plt.legend()
plt.show()

import matplotlib.pyplot as plt
plt.title('색상 바꾸기')
plt.plot([10,20,30,40],color = 'skyblue',label = '증가')
plt.plot([40,30,20,10],'red',label = '감소')
plt.legend()
plt.show()

import matplotlib.pyplot as plt
plt.title('선 스타일')
plt.plot([10,20,30,40],'r',linestyle='--',label = 'dashed')
plt.plot([40,30,20,10],'g',ls=':',label = 'dotted')
plt.legend()
plt.show()

#그래프 마커 모양 지우기
import matplotlib.pyplot as plt
plt.title('마커 모양 변경')
plt.plot([10,20,30,40],'r.',label="원(.)")
plt.plot([40,30,20,10],'g^',label="삼각형(^)")

plt.legend()
plt.show()

"""# 2. 내 생일 의 기온 변화를 그래프로 그리기


*   생일은 언제인가요
*   그날 날씨는 어땠나요?
*   기록적인 한파가 있었나요?/시원한 바람이 불었나요?
*   태어날 날부터 지금까지 매년 생일의 최고 기온을 그레프로 그린다면 어떤가요요


"""

#최고 기온의 데이터 읽어오기

filename = '/content/drive/MyDrive/부산.csv'
import csv
f = open(filename, 'r',encoding='cp949')
data = csv.reader(f,delimiter=',')
header = next(data)

for row in data:
  print(row[2])

f.close()

#데이터 리스트에 저장하기
filename = '/content/drive/MyDrive/부산.csv'
import csv
f = open(filename, 'r',encoding='cp949')
data = csv.reader(f)
next(data)
result=[]
for row in data:
  if row[2] != '':
    result.append(float(row[2]))
print(result)
print(len(result))
f.close()

"""# 2. 데이터 시각화 하기"""

filename = '/content/drive/MyDrive/부산.csv'
import csv
import matplotlib.pyplot as plt
f = open(filename, 'r',encoding='cp949')
data = csv.reader(f)
next(data)
result=[]
for row in data:
  if row[2] != '':
    result.append(float(row[2]))
f.close()
# 그래프를 추가하세요

plt.title('그래프')
plt.plot(result,color = 'skyblue')
plt.legend()
plt.show()

#그래프 크기 조절하기
plt.figure(figsize=(10,2))
plt.plot(result,'r')
plt.show()

"""# 3. 날짜 데이터 추출하기:split()함수


*   파이썬이 제공하는 문자열
*   사용자가 설정하는 특정 문자를 기준으로 문자열을 분리리


"""

s = 'Hello Python'
print(s.split())#기본적으로 공백을 기준으로 문자열을 분리리
print(s.split('Py'))

data ='2020-10-29'
#연도 출력
print(data.split('-')[0])
#월 출력
print(data.split('-')[1])
#일 출력
print(data.split('-')[2])

#split()함수를 사용해 1년 중 여름의 정점인 8월의 최고 기온 데이터만을 추출해서 그래프로 그리기
filename = '/content/drive/MyDrive/부산.csv'
import csv
import matplotlib.pyplot as plt
f = open(filename, 'r',encoding='cp949')
data = csv.reader(f)
next(data)
result=[]

for row in data:
  if row[2] != '':
    #<---여기 추가
    if row[0].split('-')[1] == '08':
      result.append(float(row[2]))
f.close()
# 그래프를 추가하세요

plt.title('그래프')
plt.plot(result,color = 'skyblue')
plt.legend()
plt.show()

filename = '/content/drive/MyDrive/부산.csv'
import csv
import matplotlib.pyplot as plt
f = open(filename, 'r',encoding='cp949')
data = csv.reader(f)
next(data)
result=[]

for row in data:
  if row[2] != '':
    #<---여기 추가
    if row[0].split('-')[1] == '05':
      if row[0].split('-')[2] == '15':
        result.append(float(row[2]))
f.close()
# 그래프를 추가하세요

plt.title('그래프')
plt.plot(result,color = 'skyblue')
plt.legend()
plt.show()

filename = '/content/drive/MyDrive/부산.csv'
import csv
import matplotlib.pyplot as plt
f = open(filename, 'r',encoding='cp949')
data = csv.reader(f)
header = next(data)

hight=[]
low=[]
for row in data:
  if row[2] != '':
    #<---여기 추가
    if 2005<= int(row[0].split('-')[0]):
      if row[0].split('-')[1] == '05':
        if row[0].split('-')[2] == '15':
          hight.append(float(row[2]))
          low.append(float(row[4]))
f.close()
# 그래프를 추가하세요

plt.title('그래프')
plt.plot(hight,color = 'skyblue')
plt.plot(low,color = 'red')
plt.legend()
plt.show()

filename = '/content/drive/MyDrive/부산.csv'
import csv
import matplotlib.pyplot as plt
f = open(filename, 'r',encoding='cp949')
data = csv.reader(f)
header = next(data)

hight=[]
low=[]
for row in data:
  if row[2] != '' and row[4] !='':
    #<---여기 추가
    if 2005<= int(row[0].split('-')[0]):
      if row[0].split('-')[1] == '05':
        if row[0].split('-')[2] == '15':
          hight.append(float(row[2]))
          low.append(float(row[4]))
f.close()
# 그래프를 추가하세요

plt.title('스승의 날의 기온 변화 그래프')
plt.plot(hight,color = 'skyblue', label='최고기온')
plt.plot(low,color = 'red', label='최저기온')
plt.show()

#hist() 함수
import matplotlib.pyplot as plt
plt.hist([1,1,2,3,4,5,6,6,7,8,10])
plt.show()

#랜덤 모듈 사용 : c언어에서와 달리 seed를 사용할 필요가 없다
import random
print(random.randint(1,6))

#주사위 시뮬레이션
import random
import matplotlib.pyplot as plt
num = 1
num1 = []
while (num<6):
  num1.append(random.randint(1,6))
  num+=1
plt.hist([num1])
plt.show()

import random
import matplotlib.pyplot as plt
num = 1
num1 = []
while (num<101):
  num1.append(random.randint(1,6))
  num+=1
plt.hist(num1,bins=11)
plt.show()

filename = '/content/drive/MyDrive/부산.csv'
import csv
import matplotlib.pyplot as plt
f = open(filename, 'r',encoding='cp949')
data = csv.reader(f)
next(data)
result=[]
for row in data:
  if row[2] != '':
    result.append(float(row[2]))
f.close()
# 그래프를 추가하세요

plt.hist(result,bins=100)
plt.show()

filename = '/content/drive/MyDrive/부산.csv'
import csv
import matplotlib.pyplot as plt
f = open(filename, 'r',encoding='cp949')
data = csv.reader(f)
next(data)
result=[]
for row in data:
  if row[2] != '':
    if row[0].split('-')[1] == '08':
      result.append(float(row[2]))
f.close()
# 그래프를 추가하세요

plt.hist(result,bins=100)
plt.show()

filename = '/content/drive/MyDrive/부산.csv'
import csv
import matplotlib.pyplot as plt
f = open(filename, 'r',encoding='cp949')
data = csv.reader(f)
plt.rc('font', family="NanumBarunGothic")
plt.rcParams['axes.unicode_minus'] = False
next(data)
result1=[]
result2=[]
for row in data:
  if row[2] != '':
    if row[0].split('-')[1] == '08':
      result1.append(float(row[2]))
    if row[0].split('-')[1] == '01':
      result2.append(float(row[2]))
f.close()
# 그래프를 추가하세요
plt.hist(result1,bins=100,label='8월')
plt.hist(result2,bins=100,label='1월')
plt.legend()
plt.show()

import random
import matplotlib.pyplot as plt

result=[]
for i in range(13):
  result.append(random.randint(1,1000))

print(sorted(result))
plt.boxplot(result)
plt.show()

import numpy as np
reult=np.array(result)
print(f'최소값 : {int(np.percentile(result,0))}')
print(f'1/4 : {int(np.percentile(result,25))}')
print(f'2/4 : {int(np.percentile(result,50))}')
print(f'최대값 : {int(np.percentile(result,100))}')

filename = '/content/drive/MyDrive/부산.csv'
import csv
import matplotlib.pyplot as plt
f = open(filename, 'r',encoding='cp949')
data = csv.reader(f)
next(data)
result=[]
for row in data:
  if row[2] != '':
    result.append(float(row[2]))
f.close()
# 그래프를 추가하세요

plt.boxplot(result)
plt.show()

filename = '/content/drive/MyDrive/부산.csv'
import csv
import matplotlib.pyplot as plt
f = open(filename, 'r',encoding='cp949')
data = csv.reader(f)
plt.rc('font', family="NanumBarunGothic")
plt.rcParams['axes.unicode_minus'] = False
next(data)
result1=[]
result2=[]
for row in data:
  if row[2] != '':
    if row[0].split('-')[1] == '08':
      result1.append(float(row[2]))
    if row[0].split('-')[1] == '01':
      result2.append(float(row[2]))
f.close()
# 그래프를 추가하세요
plt.title('1월 8월 기온 데이터')
plt.boxplot(result1)
plt.boxplot(result2)
plt.legend()
plt.show()

import matplotlib.pyplot as plt
plt.figure(figsize =(10,6))
plt.subplot(221)
plt.subplot(222)
plt.subplot(212)
plt.show()

import matplotlib.pyplot as plt
plt.figure(figsize =(10,6))
plt.subplot(411)
plt.subplot(423)
plt.subplot(424)
plt.subplot(413)
plt.subplot(414)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
t = np.arange(0,5,0.01)
plt.figure(figsize =(10,6))
plt.subplot(411)
plt.plot(t,np.sqrt(t),'r')
plt.grid()
plt.subplot(423)
plt.plot(t,t**2,'pink')
plt.grid()
plt.subplot(424)
plt.plot(t,t**3,'b')
plt.grid()
plt.subplot(413)
plt.plot(t,np.sin(t),'g')
plt.grid()
plt.subplot(414)
plt.plot(t,np.cos(t),'orange')
plt.grid()
plt.show()
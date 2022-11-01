!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf
import matplotlib.pyplot as plt
plt.rc('fount',family='NanumBarunGothic')
from google.colab import drive
drive.mount('/content/gdrive/')
dt = {}#빈 딕셔너리 만들기
for line in data:
  line = line.replace("\n","")
  items = line.split(',')
  dt[items[0]] = int (items[1])
print(type(dt))
dt
x = list (dt.keys())
y = list (dt.values())
plt.plot(x,y,'-go')
plt.title("지역평균기온")
plt.show()
for i in range(0,len(x)):
  plt.text(i,y[i],y[i],ha = 'center')
  while True:
  k = input()
  if k =='q' or k=='Q':
    break
  else:
    print(k)

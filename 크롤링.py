import requests
from bs4 import BeautifulSoup
import time
import csv
reviews = []
review_data = []
need_reviews_cnt = 1000

for page in range(1, 500):
  url = f'https://movie.naver.com/movie/point/af/list.naver/?&page={page}'
  html = requests.get(url)
  soup = BeautifulSoup(html.content,'html.parser')
  reviews = soup.find_all("td", {"class":"title"})
  for review in reviews:
    sentance = review.find("a", {"class":"report"}.get('onclick').split("', '"))[2]
    if sentance != "":
      movie = review.find("a", {"class":"movie color_b"}).get_text()
      score = review.find('em').get_text()
      review_data.append([movie.sentance, int(score)])
      need_reviews_cnt -= 1
  if need_reviews_cnt < 0:
    break
  time.sleep(0.5)
columns_name = ["movie","sentence","score"]
with open ("samples.csv","w",newline="",encoding = 'utf-8') as f:
  write = csv.writer(f)
  write.writerow(columns_name)
  write.writerows(review_data)
import pandas as pd
data = pd.read_csv("samples.csv")
data
result = data.groupby('movie')['score'].mean()
result
type(result)
result.sort_values(ascending=False)
for i in range(50):
  print(f'{i+1} : {result.index[i]}, {result[i]}점')
for i in range(len(result)):
  if 7.0 <= result[i] and result[i]<=8.0:
!apt-get update -qq
!apt-get install fonts-nanum*
!pip install konlpy
from konlpy.tag import Okt
from wordcloud import WordCloud
from collections import Counterf

movieTxt = open('samples.csv','rt',encoding='UTF-8').read()
print(movieTxt)
      print(f'{i+1}:{result, index[i]} : {result}')

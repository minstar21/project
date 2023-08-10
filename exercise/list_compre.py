students = [
    {'id': 1, 'name': 'Kim', 'score': {'math': 50, 'english': 70}},
    {'id': 2, 'name': 'Park', 'score': {'math': 80, 'english': 60}},
    {'id': 3, 'name': 'Lee', 'score': {'math': 70, 'english': 50}},
]
#print(students.values())
#영어 점수 총합이 140이상인 사람
#eng_140 = filter(lambda x, students)
#students['score'].values()
#print(students[0]['score']['english'])
#print(filter(lambda x: x['score']['english'] +  x['score']['math'] >= 140, students))
#print(list(filter(lambda x: x['score']['english'] +  x['score']['math'] >= 140, students)))

from functools import reduce
#students = [

#모든 점수의 총합을 구하는 코드(reduce)활용
#result = reduce(lambda x, y: x + sum(list(y['score'].values())), students, 0)
#print(result)

import requests

response = requests.get('https://www.naver.com')
#print(response.text)
#requests.post('주소', 보낼 데이터)

from bs4 import BeautifulSoup
# HTML 문서를 문자열 html로 저장
html = '''
<html> 
    <head> 
    </head> 
    <body> 
        <h1> 장바구니
            <p id='clothes' class='name' title='라운드티'> 라운드티
                <span class = 'number'> 25 </span> 
                <span class = 'price'> 29000 </span> 
                <span class = 'menu'> 의류</span> 
                <a href = 'http://www.naver.com'> 바로가기 </a> 
            </p> 
            <p id='watch' class='name' title='시계'> 시계
                <span class = 'number'> 28 </span>
                <span class = 'price'> 32000 </span> 
                <span class = 'menu'> 액세서리 </span> 
                <a href = 'http://www.facebook.com'> 바로가기 </a> 
            </p> 
        </h1> 
    </body> 
</html>
'''

#soup = BeautifulSoup(html, "html.parser")
#print(soup.select('.price'))
#시계 부문 가격만 가져오기(id값은 #으로 가져오기)
#print(soup.select("#watch .price"))

# 1. get 요청 보내기
#headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
#response = requests.get('https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=103#&date=%2000:00:00&page=3', headers=headers)
# 응답 제대로 왔는지 확인 필요(브라우저상 과 파이썬 상이 동일할 것이란 보장이없음)
#print(response.text)
# 2. 응답 (문자열) ->html 구조로 변환
#soup = BeautifulSoup(response.text, 'html.parser')
# 3. 변환한 데이터에서 select 써서 원하는 태그 추출
#tags = soup.select('.type06_headline li')
# 4. 태그에서 글자만 추출하도록 가공
#print(tags)
import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup
import csv

# requests 모듈을 통해서 요청보내고, html 문서받기


import requests
import csv
from bs4 import BeautifulSoup

def crawl_naver(category, date, page):
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    url = f'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1={category}&date={date}&page={page}'
    response = requests.get(headers=headers, url=url)

    soup = BeautifulSoup(response.text, 'html.parser')

    news_list = soup.select('.type06_headline li dl')

    result_list = [['제목', '본문일부', '신문사', '작성시각']]
    for news in news_list:
        try:
            title = news.select('a')[1].text.strip()
        except IndexError:
            title = news.select('a')[0].text.strip()
        content = news.select('.lede')[0].text
        writing = news.select('.writing')[0].text
        datetime = news.select('.date')[0].text
        result_list.append([title, content, writing, datetime])

    with open(f'{date}_news3.csv', 'a', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerows(result_list)

crawl_naver(104, 20230804, 1)
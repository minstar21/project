import requests
from bs4 import BeautifulSoup
import csv

# requests 모듈을 통해서 요청보내고, html 문서받기


    # requests 모듈을 통해서 요청보내고, html 문서받기
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
url = 'https://www.melon.com/chart/index.htm'
response = requests.get(headers=headers, url=url)

# 파싱하기
import requests
import csv
from bs4 import BeautifulSoup

# requests 모듈을 통해서 요청보내고, html 문서받기
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
url = 'https://www.melon.com/chart/index.htm'
response = requests.get(headers=headers, url=url)

# 파싱하기
soup = BeautifulSoup(response.text, 'html.parser')

# 원하는 정보 선택하기
titles = soup.select('.lst50 .rank01')


print(titles)
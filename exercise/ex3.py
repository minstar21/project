import csv
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
driver = webdriver.Chrome()
driver.get('https://www.melon.com/chart/month/index.htm')
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#query')))

#검색창 요소 특정
search_input = driver.find_element(By.CSS_SELECTOR, '#query')
search_input.send_keys('안녕') #검색 지시

#검색 버튼 특정
search_button = driver.find_element(By.CSS_SELECTOR, '#search-btn')
search_button.click()
time.sleep(3)
html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, 'html.parser')
titles = soup.select('.lst50. rank01. a') #리스트 리턴
artists = soup.select('.lst50. rank02. a')


import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get('https://www.melon.com/chart/month/index.htm')
# 월 선택 부분 클릭
month_selector = driver.find_element(By.CSS_SELECTOR, '#conts > div.calendar_prid > div > button')
month_selector.click()
time.sleep(3)

music_list = [['제목', '가수']]
# 특정 월을 클릭하고 곡 데이터를 출력하는 부분은 각 월마다 반복됨
for i in range(1, 7): # 1~6까지 반복
    # 특정 월 클릭
    month_element = driver.find_element(By.CSS_SELECTOR, f'#conts > div.calendar_prid > div > div > dl > dd.month_calendar > ul > li:nth-child({i}) > a')
    month_element.click()
    # 현재 html 을 변수로 저장
    time.sleep(1) # 얼마나 슬립할지는 본인 컴퓨터/인터넷 성능에 따라 결정
    html = driver.page_source
    # 파싱하기
    soup = BeautifulSoup(html, 'html.parser')
    # 원하는 정보 선택하기
    titles = soup.select('.lst50 .rank01 a')
    
    artists = soup.select('.lst50 .rank02 > a')
    for i in range(50):
        music_list.append([titles[i].text, artists[i].text])

with open('2023_melon_chart.csv', 'a', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerows(music_list)

# 드라이버 종료
driver.quit()

try:
    audio1 = md.listen()
    if audio1 == '시리야':
        while True:
            md.speak('원하는 결과를 말씀해주세요. 1. 서울 날씨, 2. 서울 미세먼지, 3. 검색, 4. 종료')
            audio2 = md.listen()
            print(audio2)
            if audio2 == '서울 날씨':
                md.weather_pm25(37.56, 126.76, '서울').get_weather() #print('결과: ' + result2)  # 인식 결과 출력
            elif audio2 == '서울 미세먼지':
                md.weather_pm25(37.56, 126.76, '서울').get_pm25weather()
            elif audio2 == '검색':
                md.speak('어떤걸 검색할까요')
                cd1.search_keyword()
            elif audio2 == '종료':
                break
            else:
                print('오류발생')
                break

except:
    print("음성 인식 실패")
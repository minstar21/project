#셀레니움 임포트
from selenium import webdriver
from selenium.webdriver.common.by import By #html 요소 탐색
from selenium.webdriver.support.ui import WebDriverWait #브라우저 응답 대기
from selenium.webdriver.support import expected_conditions as EC #html의 요소 상태 체크
import time
import module1 as md


#네이버 검색 코드 구현

def search_naver():
    text_print = md.listen()
    driver = webdriver.Chrome()
    driver.get('https://www.naver.com/')

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#query')))
    search = driver.find_element(By.CSS_SELECTOR, '#query')
    search.send_keys(text_print)
    search_button = driver.find_element(By.CSS_SELECTOR, '#search-btn')
    search_button.click()
    time.sleep(10)
    driver.quit()

#미완성
def search_tjsong():
    text_print = md.listen()
    driver = webdriver.Chrome()
    driver.get('https://www.tjmedia.com/tjsong/song_search.asp')

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#searchSong > form > ul.search2 > li > input')))
    search = driver.find_element(By.CSS_SELECTOR, '#searchSong > form > ul.search2 > li > input')
    search.send_keys(text_print)
    search_button = driver.find_element(By.CSS_SELECTOR, '#searchSong > form > ul:nth-child(6) > li > a')
    search_button.click()
    time.sleep(5)
    driver.quit()
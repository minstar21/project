from selenium import webdriver
import chromedriver_autoinstaller
import time
import os

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.implicitly_wait(3) #에러 방지를 위한 대기시간 지정

url = "https://www.instagram.com/"
driver.get(url=url)

# <input aria-label="전화번호, 사용자 이름 또는 이메일" aria-required="true" autocapitalize="off" autocorrect="off" maxlength="75" class="_aa4b _add6 _ac4d" dir type="text" value name="username">
xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'
id = os.getenv("INSTA_ID")
input_id = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
input_id.send_keys(id)
password = os.getenv("INSTA_PW")
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
#driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').send_keys(Keys.ENTER)
time.sleep(20) #접속유지 시간
#//*[@id="loginForm"]/div/div[2]/div/label/input
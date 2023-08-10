from selenium import webdriver
import chromedriver_autoinstaller
import time
chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.implicitly_wait(3) #에러 방지를 위한 대기시간 지정

url = "https://www.instagram.com/"
driver.get(url=url)
time.sleep(200) #접속유지 시간
# <input aria-label="전화번호, 사용자 이름 또는 이메일" aria-required="true" autocapitalize="off" autocorrect="off" maxlength="75" class="_aa4b _add6 _ac4d" dir type="text" value name="username">
xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'


#//*[@id="loginForm"]/div/div[2]/div/label/input
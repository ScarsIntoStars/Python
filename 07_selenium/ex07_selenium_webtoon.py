from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# 드라이버 경로설정
driver = webdriver.Chrome()
driver.get("https://comic.naver.com/webtoon")

time.sleep(5)

# 웹툰제목 크롤링
weptoonName = driver.find_elements(By.CSS_SELECTOR, '[class="ContentTitle__title--e3qXt"]')

for title in weptoonName:
    print(title.text)





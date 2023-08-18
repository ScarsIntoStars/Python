# selenium으로 유튜브 검색결과 화면 접근하기

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 크롬 브라우저 실행
driver = webdriver.Chrome()

# 접속할 주소
# driver.get("https://www.youtube.com/")

# 검색결과 페이지에 바로 접속
driver.get("https://www.youtube.com/results?search_query=르세라핌")

# 검색창 접근
search_element = driver.find_element(By.CSS_SELECTOR, 'input#search')

# 검색어 입력
# search_element.send_keys("르세라핌")


# 검색버튼 클릭
# search_click = driver.find_element(By.CSS_SELECTOR, 'button#search-icon-legacy')
# search_click.click()

# 엔터치기
search_element.send_keys(Keys.RETURN)
# time.sleep(5)

# 제목 가져오기
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

for title in titles:
    print(title.text) # innerHTML 값
   
time.sleep(5)

# https://www.youtube.com/results?search_query=르세라핌
# https://www.youtube.com/results?search_query=아이브
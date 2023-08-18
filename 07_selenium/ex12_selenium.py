from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 콘솔창에 검색어 입력
query = input("유튜브 검색어 입력 > ")

# 크롬브라우저 접근
driver = webdriver.Chrome()

# 접속할 주소
driver.get("https://www.youtube.com/results?search_query="+query)
time.sleep(5)

# 제목 가져오기
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

for title in titles:
    print(title.text) # innerHTML 값
   
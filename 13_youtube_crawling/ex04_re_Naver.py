from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 크롬 실행
start_chrome = webdriver.Chrome()

# 네이버 접속
start_chrome.get("https://www.naver.com/")

time.sleep(3)

# 검색창 접근
acc_finder = start_chrome.find_element(By.XPATH, '//*[@id="query"]')

# 검색어 입력
acc_finder.send_keys("인천 스퀘어원")

# 엔터치기
acc_finder.send_keys(Keys.RETURN)

time.sleep(2)

# 스퀘어원 식당 접근
acc_food = start_chrome.find_element(By.XPATH, '//*[@id="main_pack"]/section[3]/div/div[3]/a')

# 스퀘어원 식당 클릭
acc_food.click

time.sleep(2)
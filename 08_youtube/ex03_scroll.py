from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 크롬브라우저 접근
driver = webdriver.Chrome()
# 접속할 주소
driver.get("https://www.youtube.com/")

# javascript로 현재 페이지 높이값 가져오기
# execute_script(): javascrit 코드를 실행해주는 함수
# javascript 실행값을 파이썬 변수로 받으려면 return을 작성해야 함
# h1: 처음 페이지를 열었을 때의 높이값
h1 = driver.execute_script("return document.documentElement.scrollHeight")
print("처음높이 : ", h1)
# 스크롤을 현재높이 만큼 내리기
driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
# 영상 로딩 시간
time.sleep(5)
# 스크롤 내린 뒤 높이값
h2 = driver.execute_script("return document.documentElement.scrollHeight")
print("두 번째 높이 : ", h2)

driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
time.sleep(5)
h3 = driver.execute_script("return document.documentElement.scrollHeight")
print("세 번째 높이 : ", h3)
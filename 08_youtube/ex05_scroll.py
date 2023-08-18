# while문을 적용하여 무한스크롤 구현하기
# while문 내부 동작
# 1. 처음 높이값 확인.
# 2. 높이 만큼 스크롤 내리기.
# 3. 높이값 확인
# 4. 높이가 같다면 break로 while문 중단

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 크롬브라우저 접근
driver = webdriver.Chrome()
# 접속할 주소
driver.get("https://www.youtube.com/")


h1 = driver.execute_script("0, document.documentElement.scrollHeight")
print("처음 높이 : ", h1)

# 스크롤 후 제목데이터를 리턴하는 함수로 정의
def scroll_fun():
    while True:
        h2 = driver.execute_script("return document.documentElement.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
        time.sleep(3)
        last = driver.execute_script("return document.documentElement.scrollHeight")
        if h2==last:
            break
    # 제목 가져오기
    titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
    return titles

# 무한스크롤 함수 호출
titles = scroll_fun()


for title in titles:
    print(title.text) # innerHTML 값
print("영상 갯수 : ", len(titles))
   
    
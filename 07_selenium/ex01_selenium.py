from selenium import webdriver
import time

# 크롬 브라우저 실행
driver = webdriver.Chrome()
# 접속할 주소
driver.get("https://www.naver.com")

# 5초도안 현재상태에서 대기
time.sleep(5)
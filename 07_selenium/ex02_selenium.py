from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 크롬 브라우저 실행
driver = webdriver.Chrome()
# 접속할 주소
driver.get("https://www.example.com")

# p태그 요소만 접근하기 (element는 하나, elements는 전부)
# p_element = driver.find_element(By.TAG_NAME, 'p')
# print(p_element)
# print(type(p_element))
# print(p_element.text)

p_elements = driver.find_elements(By.TAG_NAME, 'p')
print(type(p_elements))
for p in p_elements:
    print(p.text)

# ()초동안 현재상태에서 대기
# time.sleep(10)

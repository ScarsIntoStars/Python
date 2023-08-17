from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# 드라이버 경로설정
driver = webdriver.Chrome()
driver.get("https://www.mcdonalds.co.kr/kor/menu/list.do")
# driver.maximize_window() # 최대창

time.sleep(5)

# 맥도날드 메뉴 크롤링
mc = driver.find_elements(By.CSS_SELECTOR, '[class="ko"]')
# boot = driver.find_elements(By.XPATH, '//*[@id="bd-docs-nav"]/ul/li[1]/ul/li[1]/a')

for title in mc:
    print(title.text)





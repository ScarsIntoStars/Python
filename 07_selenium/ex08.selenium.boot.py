from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# 드라이버 경로설정
driver = webdriver.Chrome()
driver.get("https://getbootstrap.com/docs/5.3/getting-started/introduction")
driver.maximize_window() # 최대창

time.sleep(5)

# 부트스트랩 doc이름 크롤링
boot = driver.find_elements(By.CSS_SELECTOR, '[class="bd-links-link d-inline-block rounded"]')
# boot = driver.find_elements(By.XPATH, '//*[@id="bd-docs-nav"]/ul/li[1]/ul/li[1]/a')

for title in boot:
    print(title.text)





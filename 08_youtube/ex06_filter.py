from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

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

# 1. 유튜브 접속
# 2. 검색어 입력
# 3. 엔터
# 4. 필터 클릭
# 5. 조회수 클릭
# 6. 무한 스크롤
# 7. 제목 수집

# 크롬브라우저 접근
driver = webdriver.Chrome()
# 접속할 주소
driver.get("https://www.youtube.com/")
# 검색창 요소 접근
search_element = driver.find_element(By.CSS_SELECTOR, 'input#search')
# 검색어 입력
search_element.send_keys("프시케")
# 엔터치기
search_element.send_keys(Keys.RETURN)
time.sleep(4)
# 필터 버튼 요소 접근
filter_button = driver.find_element(By.XPATH, '//*[@id="filter-button"]')
# filter_button = driver.find_element(By.CSS.SELECTOR, '[id="filter-button"]')
# 필터 버튼 클릭
filter_button.click()

# 조회수 XPATH
hits = driver.find_element(By.XPATH, '/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-search-filter-options-dialog-renderer/div[2]/ytd-search-filter-group-renderer[5]/ytd-search-filter-renderer[2]/a/div/yt-formatted-string')
# hits.click()
hits.click()

# 무한스크롤 함수를 출력하여 제목만 출력해봅시다
titles = scroll_fun()

for title in titles:
    print(title.text) # innerHTML 값
print("영상 갯수 : ", len(titles))

time.sleep(5)
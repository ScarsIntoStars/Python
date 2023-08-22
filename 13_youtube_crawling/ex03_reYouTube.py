from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # 얘는 엔터(return에서 사용되는 키즈임)
import time
import pandas as pd

# 무한스크롤 함수
def down_fun():
    run = True
    while run:
        h1 = start_chrome.execute_script("return document.documentElement.scrollHeight")
        start_chrome.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)") 
        time.sleep(3)
        last = start_chrome.execute_script("return document.documentElement.scrollHeight")
        if h1==last:
            run = False
        elif int(last) >= 10000:
            run = False

# 크롬 실행
start_chrome = webdriver.Chrome()

# 유튜브 접근
start_chrome.get("https://www.youtube.com/")

time.sleep(3)

# 검색창 접근
acc_finder = start_chrome.find_element(By.CSS_SELECTOR, '[name="search_query"]')

# 검색어 입력
acc_finder.send_keys("담담피아노")


# 검색버튼 클릭
finder_click = start_chrome.find_element(By.XPATH, '//*[@id="search-icon-legacy"]')
finder_click.click()

time.sleep(2)

# 무한스크롤
down_fun()

# 제목 가져오기
title_list = []
# 조회수 가져오기
hits_list = []

# 제목 요소 가져오기
titles = start_chrome.find_elements(By.CSS_SELECTOR,'[id="video-title"]')
# print(titles)

for title in titles:
    if title.get_attribute("aria-label") and title.text and "YouTube 영화" not in title.get_attribute("aria-label"):
        aria_label = title.get_attribute("aria-label")
        start_index = aria_label.find("조회수")+4
        end_index = aria_label.rfind("회")
        hits = aria_label[start_index:end_index]

        if "," in hits:
            hits = int(hits.replace(",",""))
        elif not hits:
            hits = 0
        else:
            hits = int(hits)

        if title.text not in title_list:
            title_list.append(title.text)
            hits_list.append(hits)

for title, hit in zip(title_list, hits_list):
    print(title, hit)

crawling_result = {
    "title": title_list,
    "hits": hits_list
}

pandas = pd.DataFrame(crawling_result)

pandas.sort_values(by=["hits"], ascending=False).to_csv("./pandas.csv", encoding="utf-8-sig")


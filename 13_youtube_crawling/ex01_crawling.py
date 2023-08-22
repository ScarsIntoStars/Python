from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from collections import Counter
from PIL import Image
from konlpy.tag import * 

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

def scroll_fun():
    while True:
        h2 = driver.execute_script("return document.documentElement.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
        time.sleep(3)
        last = driver.execute_script("return document.documentElement.scrollHeight")
        if h2==last:
            break

# 크롬 브라우저 실행
driver = webdriver.Chrome()

# 유튜브 인기급상승 접속
driver.get("https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl")

time.sleep(5)

scroll_fun()

# 제목 가져오기
title_list = []
# 제목 저장을 위한 리스트
hits_list = []
# 조회수 저장을 위한 리스트
scroll_fun()

titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

for title in titles:
    # shorts 영상, YouTube 영화, 제목데이터 없는 컨텐츠 
    if title.get_attribute("aria-label") and title.text and "YouTube 영화" not in title.get_attribute("aria-label"): 
        aria_label = title.get_attribute("aria-label")
        start_index = aria_label.rfind("조회수")+4
        end_index = aria_label.rfind("회")
        hits = aria_label[start_index:end_index]
        # 조회수 값 범위에 따라 분리 
        # 조회수 없는 영상은 0으로, 조회수가 1000미만인 영상은 , 처리 생략 
        # 조회수 1,000 이상 영상
        if "," in hits:
            hits = int(hits.replace(",",""))
        # 조회수 없는 영상 
        elif not hits:
            hits = 0
        # 조회수 1,000 미만 
        else:
            hits = int(hits)    
        
        # 동일한 제목 영상은 한 번만 
        if title.text not in title_list:
            title_list.append(title.text)
            hits_list.append(hits)

# 제목, 조회수 리스트 함께 조회
for title, hit in zip(title_list, hits_list):
    print(title, hit)

# 제목, 조회수 리스트가 담긴 딕셔너리
crawling_result = {
    "title": title_list,
    "hits": hits_list
}

result = pd.DataFrame(crawling_result)
# dataframe을 csv로 저장
# result.to_csv("./result.csv", encoding="utf-8-sig") 
# 조회수 내림차순으로 정렬 후 csv로 저장
result.sort_values(by=["hits"], ascending=False).to_csv("./result.csv", encoding="utf-8-sig")

okt = Okt()

for word, tag in okt.pos(title):
    print(word, tag)

# 제목 리스트에서 명사, 형용사 추출 
word_list = []
for title in title_list:
    for word, tag in okt.pos(title):
        if tag in ['Noun', 'Adjective']:
            word_list.append(word)

# 같은 단어 노출 빈도
word_list_count = Counter(word_list)

# 단어로 이루어진 리스트 생성
words = []
for word, count in word_list_count.most_common(5):
    words.append(word)

# words = [word for word, count in word_list_count.most_common(5)]
# 횟수로 이루어진 리스트 생성 
counts = [count for word, count in word_list_count.most_common(5)]
plt.bar(words, counts)
plt.show()


masking_image = np.array(Image.open('star.jpg'))

plt.axis('off') # x, y축은 필요없으므로 생략
# 결과를 이미졸 출력할 준비
plt.imshow(masking_image)
# 이미지 출력
plt.show()

# 워드클라우드 객체 생성
wc = WordCloud(font_path='malgun', background_color='white', width=400, height=400, mask=masking_image)

# Counter로 분석한 데이터를 워드클라우드로 만들기
result = wc.generate_from_frequencies(word_list_count)

# matplotlib로 이미지 출력하기
plt.axis('off') # x, y축은 필요없으므로 생략
# 결과를 이미졸 출력할 준비
plt.imshow(result)
# 이미지 출력
plt.show()


# 워드클라우드 파일 저장
wc.to_file('wordcloud_result.png')
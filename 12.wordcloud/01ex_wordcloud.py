from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt

okt = Okt()
text = "파이썬은 즐거워 파이썬은 맛있어 파이썬은 달달해 파이썬 만세 만세 만세 오늘의 점심은 파이썬이다. 내일의 점심은 파이썬이다. 오늘 저녁은 자바 내일의 저녁은 자바를 먹어야겠다."
text += "파이썬이여 당신은 왜 파이썬입니까 다른 이름도 많을텐데 파이썬이라니 너무 놀랍습니다. 파이썬은 역시 파이썬이 어울리는 이름입니다,"
text += "파이썬은 초코파이썬입니까 아니면 민초파이썬입니까 저는 민초파이썬이라면 너무 행복할 것 같습니다. 파이썬 민초파이썬 화이팅"
word_list = []
# 명사(Moun), 형용사(Adjective)만 따로 출력
for word, tag in okt.pos(text):
    if tag in ['Noun', 'Adjective']: # 명사랑 형용사만
        # print(word, tag)
        word_list.append(word)

# 같은 단어 노출 빈도
word_list_count = Counter(word_list)

# 워드클라우드 객체 생성
wc = WordCloud(font_path='malgun', width=400, height=400)

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
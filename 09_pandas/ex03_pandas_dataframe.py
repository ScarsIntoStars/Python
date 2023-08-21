import pandas as pd

scores = pd.DataFrame(
    [
        [96, 76, 64, 85 ,90], # java
        [91, 72, 44, 46 ,100], # python
        [90, 71, 78, 26 ,88] # js
    ]
)
print(scores)

scores = pd.DataFrame(
    [
        [96, 76, 64, 85 ,90], # java
        [91, 72, 44, 46 ,100], # python
        [90, 71, 78, 26 ,88] # js
    ],
    index=["java", "python", "js"]
)
print(scores)

student_number = ["짱구", "철수", "유리", "맹구", "수지"]
scores = pd.DataFrame(
    [
        [96, 88, 10],
        [76, 92, 20],
        [60, 100, 30],
        [85, 55, 40],
        [80, 70, 50]
    ],
    index=student_number
)
print(scores)

scores = pd.DataFrame(
    {
        "java":[96, 76, 64, 85 ,90], # java
        "python":[91, 72, 44, 46 ,100], # python
        "js":[90, 71, 78, 26, 88] # js
    },
    index=student_number
)
print(scores)

# 딕셔너리 데이터를 DataFrame으로 변환
score_dict = {
        "java":[96, 76, 64, 85 ,90], # java
        "python":[91, 72, 44, 46 ,100], # python
        "js":[90, 71, 78, 26 ,88] # js
}
scores = pd.DataFrame(score_dict, index=student_number)
print(scores)

# 이르 ㅁ데이터 추가
scores["이름"] = ["김파이", "이파이", "빅파이", "최파이", "정파이"]
print(scores)

# 데이터 추가
scores.loc[6] = [80, 80, 80, "조파이"]
# scores.loc["훈이"] = [80, 80, 80, "조파이"]

print(scores)

# 학번, 이름, 성적을 모두 포함한 DataFrame 선언
student_number = [1, 2, 3, 4, 5, 6]
scores = pd.DataFrame(
    {
        "이름": ["김파이", "이파이", "빅파이", "최파이", "정파이", "조파이"],
        "java":[96, 76, 64, 85 ,90, 80], # java
        "python":[91, 72, 44, 46 ,100, 70], # python
        "js":[90, 71, 78, 26 ,88, 90] # js
    },
    index=student_number
)#.transpose() 행열을 바꿈

print(scores)

# index 기준 정렬 (기본은 오름차순)
print(scores.sort_index())
# index 기준 내림차순 정렬
print(scores.sort_index(ascending=False))
# "이름"열 기준 오름차순 정렬
print(scores.sort_values(by="이름", ascending=True))
print(scores.sort_values(by="이름", ascending=False)) # 내림차순
# python 기준 오름차순 정렬
print(scores.sort_values(by="python", ascending=True))

# 첫 2줄만 조회
print(scores.head(2))
print(scores.tail(2))

# DataFrame을 csv로 내보내기
scores.to_csv("./scores.csv", encoding="utf-8-sig")
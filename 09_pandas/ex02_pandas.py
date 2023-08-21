import pandas as pd

# 성적 다루는 간단한 예제
# 학번 정보
student_number = [1, 2, 3, 4, 5]

score_java = pd.Series([10, 20, 30, 40, 50], index=student_number)
score_python = pd.Series([100, 200, 300 ,400, 500], index=student_number)

print(score_java)
print(score_python)

# java, python 시리즈 합계
total = score_java + score_python
print(total)

score_js = pd.Series([3, 2, 1, 4, 5], index=[3, 2, 1, 4, 5])
# print(score_js)
# index 값 기준으로 정렬하여 출력
# print(score_js.sort_index())

# java, python, js 총 합계
total = score_java + score_python + score_js
print(total)

# index 기준 내림차순 정렬
print(total.sort_index(ascending=False))

# 값 기준 오름차순 정렬
print(total.sort_values(ascending=False))
# 딕셔너리(dictionary): 매핑형(key, value) 자바의 해쉬맵같은 것
word_dic ={
    "dog" : "강아지",
    "cat" : "야옹이",
    "tiger" : "호양이",
    "lion" : "사자"
}
print(word_dic)
print(word_dic["dog"])
# 기존 value 수정
word_dic["dog"] = "멍멍이"
# 새로운 데이터 추가
word_dic["bear"] = "곰"

print(word_dic)

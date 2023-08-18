# 조회수값 추철하기

aria_label = "LE SSERAFIM 조회수 (르세라핌) 'ANTIFRAGILE' OFFICIAL M/V 게시자: HYBE LABELS 10개월 전 3분 52초 조회수 183,866,871회"


# rfind(): 매개변수로 전달한 글자의 인덱스 값을 변환(해당 변수의 제일 마지막에서 시작하여 찾음)
# find(): 해당 변수의 시작지점부터 찾음

print(aria_label.rfind("조회수")) # 뒤에서부터 찾아라 "조회수"가 몇 번 인덱스에 있는 지
print(aria_label.find("조회수")) # 앞에서부터 찾아라 "조회수"가 몇 번 인덱스에 있는 지

# 조회수 값의 시작 인덱스 값
print(aria_label.rfind("조회수")+4)
# print(aria_label[85]) # 1
# 조회수 값의 끝 인덱스 값
print(aria_label.rfind("회"))
# print(aria_label.rfind([96])) # 1

# 조회수 값만 출력하기
print(aria_label[85:96])

start_index = aria_label.rfind("조회수")+4
end_index = aria_label.rfind("회")
hits = aria_label[start_index:end_index]

print(hits)
print(type(hits))
# 쉼표 제거 후 정수형으로 변환
# replace(): 바꾸기 기능
hits = int(hits.replace(",",""))
print(hits)
print(type(hits))
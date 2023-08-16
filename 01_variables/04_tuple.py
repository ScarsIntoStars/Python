# 튜플 - 투플은 값의 재할당이 안됨(변경못함)
int_tuple = (1, 2, 3, 4)
print(int_tuple)
print(int_tuple[1])
print(int_tuple[2])
#int_tuple[2] = 10
print(int_tuple[2])

str_tuple = ("hello", "안녕하세요", "ㅎㅎㅎ")

mix_tuple = (1, 3, "ㅎㅎㅎ", "파이썬")

tuple_in_tuple = ("안녕", (1, 10, "ㅎㅎㅎ"), "hello", 1.23)
print(mix_tuple)
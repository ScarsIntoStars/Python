# 구구단을 함수로 ex03_function.py에 각각 정의하고
# main에서 1, 2번을 선택해 받아 세로형, 가로형을 각각
# 출력할 수 있도록 하시오.

from ex03_function import *


num = input("1: 세로형 구구단   2:가로형 구구단   3:종료")
if num=="1":
    print("세로")
    table_odd()
elif num=="2":
    print("가로")
    table_even()
else:
    print("종료")



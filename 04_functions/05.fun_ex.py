# 실행하면 콘솔에서 1 또는 2를 입력받고, 1은 세로형구구단, 2는 가로형구구단을 각각 출력한다.
# 구구단은 각각 함수로 정의하도록 한다.

num = input("1 : 세로출력  2 : 가로출력 > ")

print(type(num))

def table_even():
    for i in range(2, 10):
        for j in range(1, 10):
            print(i,"x",j,"=",i*j)

    
def table_odd():
    for i in range(2, 10):
        for j in range(1, 10):
            print(i,"x",j,"=",i*j, end="  ")
        print()



if num==str(1):
    print("구구단 세로출력")
    table_even()

elif num==str(2):
    print("구구단 가로출력")
    table_odd()

else:
    print("숫자를 입력하세요!")




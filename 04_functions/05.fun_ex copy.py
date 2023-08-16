# 실행하면 콘솔에서 1 또는 2를 입력받고, 1은 세로형구구단, 2는 가로형구구단을 각각 출력한다.
# 구구단은 각각 함수로 정의하도록 한다.

def table(n):
    if n==1:
        for i in range(2, 10):
            for j in range(1, 10):
                print(i,"x",j,"=",i*j)
    else:
        for i in range(2, 10):
            for j in range(1, 10):
                print(i,"x",j,"=",i*j, end="  ")
            print()


num = int(input("1 : 세로출력  2 : 가로출력 > "))

print(type(num))

table(num)
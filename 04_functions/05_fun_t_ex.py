
def fun1():
    #세로형
    for i in range(2, 10):
        for j in range(1, 10):
            print(i,"x",j,"=",i*j)

def fun2():
    for i in range(2, 10):
        print(i, "단")
        for j in range(1, 10):
            print(i,"x",j,"=",i*j, end="  ")
        print()




run = True
while run:
    sel = int(input("선택: "))
    if sel ==1:
        # print("1번을 선택했습니다")
        fun1()
    elif sel ==2:
        # print("2번을 선택했습니다")
        fun2()
    elif sel ==3:
        print("종료")
        run = False

print("종료되었습니다")
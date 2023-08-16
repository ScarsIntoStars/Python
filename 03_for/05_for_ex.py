# 중첩 for문을 이용하여 구구단을 세로형, 가로형으로 각각 만들어봅시다.

dan = "단"

# 가로형
for i in range(2, 10):
    print (str(i)+(dan))
    for j in range(1, 10):
        print(i, "x", j, "=", i*j, end="  ")
    print()
print()
# 세로형
for i in range(2, 10):
    print (str(i)+(dan))
    for j in range(1, 10):
        print(i, "x", j, "=", i*j)
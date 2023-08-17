def table_odd():
    for i in range(2, 10):
        for j in range(1,10):
            print(i, "X", j, "=", i*j)

def table_even():
    for i in range(2, 10):
        print(i,"단")
        for j in range(1, 10):
            print(i, "X", j, "=", i*j, end="  ")
        print()
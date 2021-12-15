def swap(a, b):
    temp = b
    b = a # b에 있는 2가 없어짐
    a = temp
    print(a, b)

swap(1, 2) # 2 1
swap(3, 4) # 4 3

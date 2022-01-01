def multiple(a, b):
    # a가 b의 배수인지 아닌지 T, F
    # 10이 2의 배수인가?
    remainer = a % b
    return remainer

print(multiple(10, 2))
print(multiple(5, 2))
print(multiple(11, 2))

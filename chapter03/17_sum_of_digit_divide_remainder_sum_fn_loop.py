def sum_digit(num):
    r = 0

    while num > 0:
        r += num % 10 # 668-- 7
        num = num // 10 # 668 - 66 - 6 - 0
    return r

print(sum_digit(1956687))
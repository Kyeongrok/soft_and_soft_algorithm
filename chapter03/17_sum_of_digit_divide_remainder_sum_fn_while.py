def sum_digit(num):
    # for num type 숫자
    r = 0
    # 몫이 0보다 큰 동안 687 68 6 0
    while num > 0:
        r += num % 10
        num = num // 10
    return r

print(sum_digit(6687))
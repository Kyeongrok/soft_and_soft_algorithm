def sum_digit(num):
    r = 0
    r += num % 10
    num = num // 10
    r += num % 10
    num = num // 10
    r += num % 10
    return r

print(sum_digit(687))
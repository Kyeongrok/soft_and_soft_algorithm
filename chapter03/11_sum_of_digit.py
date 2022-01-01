def sum_of_digit(n):
    s_n = str(n)
    result = 0
    for c in s_n:
        # print(c, type(c), int(c))
        result += int(c)
    return result

print(sum_of_digit(123))
print(sum_of_digit(678))
print(sum_of_digit(6678))

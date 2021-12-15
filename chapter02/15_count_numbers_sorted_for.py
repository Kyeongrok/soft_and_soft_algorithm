from collections import Counter
numbers = [4, 0, 4, 4, 1, 8, 8, 2, 2, 5, 0, 6, 5, 6, 0]
memo = [0] * 10
print(len(memo), memo)
print('counter:', Counter(numbers))

for n in numbers:
    memo[n] += 1

for i in range(len(memo)):
    print(i, memo[i])
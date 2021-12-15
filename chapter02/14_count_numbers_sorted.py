from collections import Counter
numbers = [4, 0, 4, 4, 1, 8, 8, 2, 2, 5, 0, 6, 5, 6, 0]
strs = ['t', 'e', 's', 't']
print(len(numbers))

numbers = sorted(numbers)
c = Counter(numbers)
print(c)

for key, value in c.items():
    print(key, value)
# s = '()((()))'
s = '(((('

for i in range(len(s) - 1):
    # i = 0
    if s[i] == '(' and s[i+1] == ')':
        print(i, s[i])

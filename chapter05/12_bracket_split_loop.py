# s = '()((()))'
s = '((('

for i in range(len(s)):
    # i = 0
    if s[i] == '(' and s[i+1] == ')':
        print(i, s[i])

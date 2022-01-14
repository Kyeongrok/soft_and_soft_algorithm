s = '()((()))'

for i in range(len(s) - 1):
    # i = 0
    if s[i] == '(' and s[i+1] == ')':
        # remove
        left = s[:i] # 0
        right = s[i+2:] # 2
        print(left + right)

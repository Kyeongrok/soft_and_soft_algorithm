def solution(s):

    while '()' in s: # s안에 ()가 있는 동안
        for i in range(len(s)):
            if s[i] == '(' and s[i+1] == ')':
                # remove
                left = s[:i] # 0
                right = s[i+2:] # 2
                s = left + right
                break
    return len(s) == 0


print(solution('()((()))'))
print(solution('()((()))('))
print(solution(')')) # False
# print(solution('('*50_000 + ')'*50_000))

def solution(s):
    while '()' in s:
        sp = s.split('()')
        s = ''.join(sp)
    return len(s) == 0

print(solution('()((()))'))
print(solution('()((()))('))
print(solution(')')) # False

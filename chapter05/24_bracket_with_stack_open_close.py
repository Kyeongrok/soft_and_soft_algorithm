
def solution(s):
    for c in s:
        if c == '(':
            print('여는 괄호')
        elif c == ')':
            print('닫는 괄호')

s = '()((()))'
solution(s)

def solution(s):
    while '()' in s:
        sp = s.split('()')
        s = ''.join(sp)
    return len(s) == 0

from datetime import datetime
start = datetime.now()
print(solution('('*500_000 + ')'*500_000))
print(datetime.now() - start)

from st1 import Stack1

def solution(s):
    st = Stack1()  # []
    for c in s:
        if c == '(': # 여는 괄호
            st.push(c)
        elif c == ')': # 닫는 괄호
            if st.empty():
                return False
            st.pop()
    return st.empty()

print('r:', solution('()((()))'))
print('r:', solution('()((()))('))
print('r:', solution(')()((()))('))

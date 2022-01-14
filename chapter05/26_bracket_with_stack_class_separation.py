from st1 import Stack1

st = Stack1() # [(]
s = '()((()))('
for c in s:
    if c == '(': # 여는 괄호
        st.push(c)
    elif c == ')': # 닫는 괄호
        st.pop()

print(s, st.empty())


class Stack1():

    arr = []
    last_index = 0 # 1 + 1 = 2

    def __init__(self, size=10000):
        self.arr = [None] * size

    def push(self, value):
        self.arr[self.last_index] = value
        self.last_index += 1

    def pop(self):
        if self.empty():
            raise Exception('Stack is empty.')
        value = self.arr[self.last_index - 1]
        self.last_index -= 1
        return value

    def empty(self):
        return self.last_index == 0


    def peek(self):
        if self.empty():
            raise Exception("Stack is empty.")
        return self.arr[self.last_index - 1]


st = Stack1() # [(]
s = '()((()))('
for c in s:
    if c == '(': # 여는 괄호
        st.push(c)
    elif c == ')': # 닫는 괄호
        st.pop()

print(s, st.empty())


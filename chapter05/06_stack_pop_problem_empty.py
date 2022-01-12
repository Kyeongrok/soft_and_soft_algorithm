class Stack1():

    arr = []
    last_index = 0 # 1 + 1 = 2

    def __init__(self, size=10000):
        self.arr = [None] * size

    def push(self, value):
        self.arr[self.last_index] = value
        self.last_index += 1

    def pop(self):
        if self.last_index <= 0:
            raise Exception('Stack is empty.')
        value = self.arr[self.last_index - 1]
        self.last_index -= 1
        return value

st = Stack1()
print(st.pop())
st.push(45)
print(st.arr[:10])

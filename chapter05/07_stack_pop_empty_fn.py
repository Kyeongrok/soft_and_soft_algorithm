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

st = Stack1()
st.pop()
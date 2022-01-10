class Stack1():

    arr = []

    def __init__(self, size=10000):
        self.arr = [None] * size

    def push(self, value):
        self.arr[0] = value

st = Stack1()
st.push(15)
st.push(20)
print(len(st.arr))
print(st.arr)

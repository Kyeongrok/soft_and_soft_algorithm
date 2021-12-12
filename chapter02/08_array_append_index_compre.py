string = 'ABCDEDE'


l1 = ['A' for i in range(len(string))]

print('before:', l1)
l1[0] = 1
print('after:', l1)
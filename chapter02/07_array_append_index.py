string = 'ABCDEDE'

l1 = [] # list != arr
for i in range(len(string)):
    l1.append(0)

print('before:', l1)
l1[0] = 1
print('after:', l1)
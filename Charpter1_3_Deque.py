# Created by Yi Xie 6/25/2019
# Examples on Python Cookbook

from collections import deque
q = deque(maxlen=4)
q.append('a')
print(q)
q.appendleft('b')
print(q)
q.append('c')
q.append('d')
print(q)
q.appendleft('e')
print(q)

print('--------------------------------------------')

data_set = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for ele in data_set:
    q.append(ele)
print(q)

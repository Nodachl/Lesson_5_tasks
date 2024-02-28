import random

lst = []
for i in range(10):
    lst.append(random.randint(-10, 10))

new_lst = []
for i in lst:
    if i % 2 == 0:
        new_lst.append(i)

print(new_lst)

new_lst = []
for i in lst:
    if i % 2 != 0:
        new_lst.append(i)

print(new_lst)

new_lst = []
for i in lst:
    if i < 0:
        new_lst.append(i)

print(new_lst)

new_lst = []
for i in lst:
    if i > 0:
        new_lst.append(i)

print('positive numbers:', new_lst)



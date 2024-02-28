import random

lst = []
for i in range(10):
    lst.append(random.randint(-10, 10))

print(lst)
cum_sum_negative = 0
cum_sum_even = 0
cum_prod_3 = 1
for i in range(len(lst)):
    if lst[i] < 0:
        cum_sum_negative += lst[i]
    if lst[i] % 2 == 0:
        cum_sum_even += lst[i]


    if i % 3 == 0:
        cum_prod_3 *= lst[i]  # same as cum_prod_3 = cum_prod_3 * lst[i]

lst.sort()
print(cum_prod_3)

cum_5 = 1
for i in lst[1:-1]:
    cum_5 *= i

cum_6 = 0
lst = [i for i in lst if i >= 0]
print(lst)
for i in lst[1:-1]:
    cum_6 += i
print(cum_6)
# print('sum of negatives:', cum_sum_negative)
# print('sum of evens:', cum_sum_even)
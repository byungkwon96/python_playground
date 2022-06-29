# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

# product calculate cartisian product of two array
from itertools import product

a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(list(prod))

b = [3]
prod = product(a, b, repeat=2)
print(list(prod))

# permutations returns all possible ordering
from itertools import permutations

a = [1, 2, 3]
perm = permutations(a)
print(list(perm))
perm = permutations(a, 2)
print(list(perm))

# combinations all poosible combination of specific length
from itertools import combinations, combinations_with_replacement

print("Combinations")
a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))
print("Combinations with replacement")
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

# accumlate the sum
from itertools import accumulate

print("Accumulate")
acc = accumulate(a)
print(a)
print(list(acc))

import operator

acc = accumulate(a, func=operator.mul)
print(list(acc))

# returns keys from iterable
from itertools import groupby


def smaller_than_3(x):
    return x < 3


print("Group by object")
# group_obj = groupby(a, key=lambda x: x<3)
group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))

# infinite iterator
from itertools import count, cycle, repeat

"""
for i in count(10):
    print(i)
    if i == 15:
        break
"""

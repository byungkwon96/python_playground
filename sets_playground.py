# Sets: unordered, mutable, no duplicates
myset = {1, 2, 3, 3}
print(myset)

# can use list or string
myset = set("Hello")
print(myset)

myset = set([1, 2, 3])
print(myset)

# empty set
myset = set()
print(type(myset))

# add elements
myset.add(1)
myset.add(2)
myset.add(3)
print(myset)

# remove elements
myset.discard(4)  # without error

# clear
# myset.clear()

# pop
print(myset.pop())

# iterate
for i in myset:
    print(i)

# if statement
if 2 in myset:
    print("yes 2 is in the set")

# union of sets
odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8}

unionNum = odds.union(evens)
print(unionNum)

# intersection
intersectOddEven = odds.intersection(evens)
print(intersectOddEven)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

# diff of set == A-B
diffA = setA.difference(setB)
print(diffA)

# A-B + B-A
diffsym = setA.symmetric_difference(setB)
print(diffsym)

# update adds missing elements
# setA.update(setB)
# print(setA)

# intersection update and difference update symmetric
# setA.difference_update(setB)
# setA.intersection_update(setB)
# setA.symmetric_difference_update(setB)

# SuperSet, subset same in math
setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
print(setB.issubset(setA))
print(setA.issuperset(setB))

# disjoint checks the whether sets are disjoint
setC = {7, 8}
print(setA.isdisjoint(setC))

# copy only equals means same reference
setA = setB.copy()

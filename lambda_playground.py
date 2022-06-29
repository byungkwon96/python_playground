# lambda arguments: expression
add10 = lambda x: x + 10
print(add10(5))

# multiple arguments lambda
mult = lambda x, y: x * y
print(mult(3, 7))

# sorted list
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D)
points2D_sorted_Y = sorted(points2D, key=lambda x: x[1])
print(points2D_sorted)
print(points2D_sorted_Y)

# map(func, seq)
print("Map")
a = [1, 2, 3, 4, 5]
# b = [x*2 for x in a] === is same as below
b = map(lambda x: x * 2, a)
print(list(b))

# filter(func,seq) returns all the true value
# b = [x for x in a if x%2==0]
print("Filter")
b = filter(lambda x: x % 2 == 0, a)
print(list(b))

# reduce(func,seq)
from functools import reduce

print("REDUCE")
product_a = reduce(lambda x, y: x * y, a)
print(product_a)
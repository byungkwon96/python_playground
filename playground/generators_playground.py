def mygenerator():
    yield 1
    yield 2
    yield 3


g = mygenerator()
print(g)

# for i in g:
#    print(i)

# raises stop iteration when it finished
value = next(g)
print(value)


def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1


cd = countdown(4)

value = next(cd)
print(value)

print(next(cd))

# generator is memory efficient
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums


def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


fib = fibonacci(30)
for i in fib:
    print(i)

mygenerator1 = (i for i in range(10) if i % 2 == 0)
for i in mygenerator1:
    print(i)
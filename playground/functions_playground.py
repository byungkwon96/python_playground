"""
1) The difference between arguments and parameters
2) Positional and keyword arguments ex)foo(b=1,c=2,a=3)
3) Default arguments -- ex)def foo(a,b,c,d=4)
4) Variable-length arguments (*args and **kwargs)
5) Container unpacking into function arguments
6) Local vs. global arguemtns
7) Parameter passing (by value or by reference) -- pointer or value 
"""

# args any number of arguments, kwargs any number of keyword arguments
def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])


foo(1, 2, 3, 4, 5, six=6, seven=7)

# unpacking
def ba(a, b, c):
    print(a, b, c)


mylist = [0, 1, 2]  # tuple also works
ba(*mylist)  # unpacking -- but length must match the parameter

my_dict = {"a": 1, "b": 2, "c": 3}
ba(**my_dict)  # for dictionary needs **

# * * * * * * * * * *
# 3 * 7 multiplication
# 2 ** 4 power
zeros = [0] * 10  # create list, tuples, strings
# use as *args, **kwargs
first, *others = zeros  # can unpack with

# deep copy
# import copy
# cpy = copy.deepcopy

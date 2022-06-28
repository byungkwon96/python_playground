# tuples cannot changed after created
# tuple is faster in interation and smaller in size than list
mytuple = ("Max", 28, "Boston")
print(mytuple)

# one item in a tuple
mytuple = ("Max",)

# refering item in the tuples
item = mytuple[0]
print(item)

# Tuples are immutable
# mytuple[0] = "hi"  #doesn't work

# check item in a tuple
if "Max" in mytuple:
    print("yes")
else:
    print("no")

len(mytuple)
print(mytuple.count("a"))
print(mytuple.index("Max"))

# transform list and tuple
my_list = list(mytuple)
mytuple = tuple(my_list)

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

b = a[2:5]
print(b)

# reverse
b = a[::-1]
print(b)

mytuple = ("Max", 28, "Boston")
# unpack
name, age, city = mytuple
print(city)

# u can upack with *
i1, *i2, i3 = a
print(i2)

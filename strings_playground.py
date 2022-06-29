# Strings: ordered, immutable, text representation
my_string = "Hello World"
print(my_string)
my_string = "hello"
print(my_string)

# multi-line
my_string_multiline = """Hello 
World"""
print(my_string_multiline)

# char
char0 = my_string[0]
print(char0)

# substring with slicing
substring = my_string[1:4]
print(substring)

# add string with +
name = "Bob"
setence = my_string + " " + name
print(setence)

# iteration
for i in my_string:
    print(i)

# if statement
if "ello" in my_string:
    print("yes ello")

# remove white place with strip()
my_string = "        Hello world    "
print(my_string)
my_string = my_string.strip()
print(my_string)

# convert upper and lower
print(my_string.upper())
print(my_string.startswith("H"))
print(my_string.endswith("ello"))

# doesn't find substring or character it returns -1
print(my_string.find("lo"))

# count
print(my_string.count("o"))

# replace
print(my_string.replace("world", "Bob"))
print(my_string)  # doesn't change original because string is immutable

# string to list
my_list = my_string.split()
print(my_list)  # split each sapce by default

# list to string
new_string = " ".join(my_list)  # " " <- puts inbetween elements
print(new_string)

# %, .format(), f-strings
var = "Bob"
my_string = "the variable is %s" % var  # % is a place holder (%s, %d, %f)
print(my_string)
my_string = "the variable is {}".format(var)  # use {} and format (:2.f)
my_string = f"The variable is {var}"  # put f infront
print(my_string)

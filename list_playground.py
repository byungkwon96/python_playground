# Lists
mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist2 = list()
print(mylist2)

item = mylist[2]
print(item)

item2 = mylist[-1]
print(item2)

# for loop of my list
for i in mylist:
    print(i)

# check whether item is in a list
if "apple" in mylist:
    print("Yes it is in!")
else:
    print("no")

# lenght of list
print(len(mylist))

# inserting, and appending
mylist.append("lemmon")

mylist.insert(1, "watermelon")
print(mylist)

# remove, and popping
itemPopped = mylist.pop()
print(itemPopped)
print(mylist)

# it doesn't work when item spelled it wrong
itemRemoved = mylist.remove("apple")
print(itemRemoved)

# item = mylist.clear() -> clear
mylist.reverse()
print(mylist)

# item = mylist.sort() -> asending order
new_list = sorted(mylist)
print(mylist)
print(new_list)

# slicing
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = a[1:5]
print(b)
b = a[::2]  # stepping index by 2
print(b)

# copying mylist.copy() || list(mylist)
list_copy = mylist.copy()
list_copy[0] = "lemon"
print(list_copy)

# list: ordered, mutable, allows duplicate elements
a = [1, 2, 3, 4, 5, 6]
b = [i * i for i in a]
print(b)

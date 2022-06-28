# Dictionrary: Key-value paires, unordered, mutable
mydict = {"name": "Bob", "age": 28, "city": "Boston"}
print(mydict)

mydict2 = dict(name="ha", age=27, city="CA")
print(mydict2)

# value
value = mydict["name"]
print(value)

# add key value
mydict["email"] = "abc@abc.com"
print(mydict)

# delete mydict.pop("email"), mydict.popitem()
del mydict["email"]
print(mydict)

# throws an exception if the key doesn't exist so use try or if
if "name" in mydict:
    print(mydict["name"])
else:
    print("doesn't exist")

try:
    print(mydict["city"])
except:
    print("Error")

# iteration mydict.keys()
for key in mydict:
    print(key)

for value in mydict.values():
    print(value)

for key, value in mydict.items():
    print([key, value])

# copy the dictionary or dict(mydict)
mydict_copy = mydict.copy()

# combining dictionary data is updated and non existing keys are added
mydict.update(mydict2)
print(mydict)

# can use tuple as keys not list
mytuple = (8, 7)
mydict = {mytuple: 15}
print(mydict)
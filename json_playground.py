# handling Json file in python (serilization, encoding)
import json

person = {"name": "ha", "age": 30, "city": "Seoul"}

personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

# write in the person.json file
with open("person.json", "w") as file:
    json.dump(person, file, indent=4, sort_keys=True)

# json to dictionary (decoding)
person = json.loads(personJSON)
print(person)

# open json file
with open("example.json", "r") as file:
    person = json.load(file)

# custom class
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Max", 27)

# custom encoding function because user is customized class
def encode_user(o):
    # checks whether obejct o is a obejct of User Class
    if isinstance(o, User):
        return {"name": o.name, "age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Object of type User is not Json serialable")


from json import JSONEncoder


class UserEncoder(JSONEncoder):
    def default(self, o):
        # checks whether obejct o is a obejct of User Class
        if isinstance(o, User):
            return {"name": o.name, "age": o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)


# userJson = json.dumps(user, default=encode_user)
userJSON = UserEncoder().encode(user)

# decoder the user class
user = json.loads(userJSON)  # returns as dictionary so needs decoding method


def decode_user(dct):
    if User.__name__ in dict:
        return User(name=dct["name"], age=dct["age"], object_hook=decode_user)
    return dct

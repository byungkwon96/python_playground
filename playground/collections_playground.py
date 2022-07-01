# collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter

a = "aaaaabbbbccc"
# counter makes it a dictionary
my_counter = Counter(a)
print(my_counter)
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(2))  # returns list of tuples
print(list(my_counter.elements()))

# tuple
from collections import namedtuple

Point = namedtuple("Point", "x,y")
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)

# ordered Dict
from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict["a"] = 1
ordered_dict["b"] = 2
ordered_dict["c"] = 3
print(ordered_dict)

# default dict - default value if key is not set
from collections import defaultdict

d = defaultdict(int)
d["a"] = 1
d["b"] = 3
print(d)
# if it doesn't exisst it returns default value for int it is 0
print(d["4"])

# deque double ended queue
from collections import deque

deqTest = deque()
deqTest.append(1)
deqTest.append(3)
print(deqTest)

deqTest.appendleft(5)
print(deqTest)
deqTest.pop()
print(deqTest)
deqTest.popleft()
print(deqTest)
deqTest.extendleft([4, 5, 6])
print(deqTest)
deqTest.rotate(2)
print(deqTest)
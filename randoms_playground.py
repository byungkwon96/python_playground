# generate sudo random
import random

# print random range(0,1)
a = random.random()

a = random.uniform(1, 10)

# include upperbound
a = random.randint(1, 10)

# upperboudn not included
a = random.randrange(1, 10)

# statistics mean = 0, standardiviation = 1
a = random.normalvariate(0, 1)

# can pick random element in the list
mylist = list("ABCDEFGH")
a = random.choice(mylist)

# more UNIQUE elements in the list
a = random.sample(mylist, 3)

# can pick same element multiple times
a = random.choices(mylist, k=3)

# shuffle the list
random.shuffle(mylist)

# can get seed because it is sudo random
random.seed(1)  # will give same numbers if the seed is same

import secrets  # security tokens, password since random is not really random

# secrets are slower
# 3 functions
a = secrets.randbelow(10)  # produce ranInt
print(a)

a = secrets.randbits(4)  # produce bits #ex)1010 max=15

mylist = list("ABCDEFGH")
a = secrets.choice(mylist)

import numpy as np

# can create matrix
a = np.random.rand(3, 3)
print(a)
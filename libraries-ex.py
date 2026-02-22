# There are two types of import types

# First
# imports compelete library
import math

square_root = math.sqrt(16)
print(square_root)
print(math.pi)

# Second

# imports specific items from the library
from math import sqrt, pi

sqrt(16)
pi

# This library pick random values
import random
number = random.randint(1, 10)
choice = random.choice(["apple", "banana", "orange"])


# Date and time library
import datetime
today = datetime.date.today()
print(today)
#  LIST
age = 25
has_licence = False

my_list =["Alice",25,age,True,has_licence]

my_list[0]
age = my_list[1]
has_licence = my_list[-1]  #for last element
has_licence = my_list[-2]


my_list[0]= "Dave"

my_list.append("Alice")

my_list.insert(1,"Alice")

my_list.remove("Alice")

# DICTIONARIES


person = {
    "name":"Alice",
    "age":25,
    "city":"New-York"
}

person["name"]="Dave"

person["licence"]= True

del person["licence"]

# TUPLES

# Empty tuple
empty = ()

# Tuple with items
point = (3, 5)
colors = ("red", "green", "blue")

colors[0]

# SETS

# Empty set (careful!)
empty_set = set()  # NOT {} - that's a dict!

# Set with values - both ways work
numbers = {1, 2, 3, 4, 5}
fruits = set(["apple", "banana", "orange","banana"])

# From a list (removes duplicates)
scores = [85, 90, 85, 92, 90]
unique_scores = set(scores)  # {85, 90, 92}

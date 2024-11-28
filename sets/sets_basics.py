courses = {'Physics', 'Chemistry', 'Maths', 'Biology', 'Maths'}

print(courses)   # Automatically removes duplicate
print('Biology' in courses)   # Returns true or False

set_1 = {1, 5, 7, 8}
set_2 = {2, 3, 4, 5, 6, 7}

print(set_1.intersection(set_2))   # items that are common in both sets
print(set_1.union(set_2))   # items that are in set_1 and set_2
print(set_1.difference(set_2))   # items that are in set_1 and not in set_2

# Empty List
empty_list = []
empty_list = list()

# Empty Tuple
empty_tuple = ()
empty_tuple = tuple()

# Empty Set
empty_set = {}   # this will not work, it will create an empty dictionary
empty_set = set()

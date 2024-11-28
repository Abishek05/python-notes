courses = ['Physics', 'Chemistry', 'Maths', 'Biology']

print(courses)

# enumerate will return 2 values, item and the index of that item
for index, course in enumerate(courses):
    print(index, course)

# start from index 1, in this case it will start from 1 not 0
for index, course in enumerate(courses, start=1):
    print(index, course)

# to get CSV values of list in string
courses_str = ' , '.join(courses)
print(courses_str)
print(type(courses_str))

# to split string and get list
new_list = courses_str.split(' , ')
print(new_list)

courses = ['Physics', 'Chemistry', 'Maths', 'Biology']

courses.append('Computer')   # to add item to the end of list
print(courses)

courses.insert(0, 'Electronics')   # to insert new item at a specified index
print(courses)

courses_2 = ['Art', 'Education']

# append or insert list to a list i.e, list of list [[1, 2], 3, 4, 5]
courses.append(courses_2)
courses.insert(0, courses_2)
print(courses)

# extend the list to add each individual items of one list to the other
courses.extend(courses_2)
print(courses)

# remove items from the list
courses.remove('Maths')
print(courses)

# remove last item from list
value = courses.pop()   # it returns the removed value
print(courses)
print(value)

courses.reverse()   # to reverse a list
print(courses)

courses_3 = [3, 1, 9, 4, 2]
courses_3.sort()   # sort will make it ascending
print(courses_3)
courses_3.sort(reverse=True)   # sort will make it descending if reverse=True
print(courses_3)

# to sort without altering the original list
courses_4 = [4, 8, 1, 5, 9]
sorted_list = sorted(courses_4)
print(courses_4)
print(sorted_list)

print(min(courses_4))   # Minimum value in a list
print(max(courses_4))   # Maximum value in a list
print(sum(courses_4))   # Sum of all items in a list

# finding values in a list
print(courses_4)
print(courses_4.index(8))

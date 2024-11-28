message = "Hello World"

print(message.lower())   # To lower case the string
print(message.upper())   # To upper case the string
print(message.count("l"))   # To count certain number of characters in a string

# To find the index of where a certain characters can be found
print(message.find('l'))
print(message.find('World'))

print(message.find('Universe'))   # Returns -1 if it cannot find

# To replace string, note it will not replace it in the variable message but will return the new string
print(message.replace('World', 'Universe'))

# To Concatenate String
greeting = 'Hello'
name = 'Lucy'

message = greeting + name
print(message)

message = greeting + ' ' + name
print(message)

message = '{} {}'.format(greeting, name)
print(message)

# In python 3.6 or higher only f strings will work
message = f'{greeting} {name}'
print(message)

# In f strings we can write code within the placeholders
message = f'{greeting} {name.lower()}'
print(message)

print(dir(message))   # dir method for string
print(help(str))   # help method for string
print(help(str.lower))   # help method for string specific method


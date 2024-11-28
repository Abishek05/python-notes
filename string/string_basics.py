message = "Hello World"

print(message)
print(len(message))   # Length of the String

# Access String characters individually
print(message[0])   # Access 1st character in a string
print(message[10])   # Access value at index 10

# Try to access the index of string that doesn't exist we get - IndexError: String index out of range

# Slicing of String
print(message[0:4])   # Access range of the characters (1st index is inclusive of value, 2nd index is not)
print(message[:4])   # If we leave off the 1st index it will assume we want to start at the beginning
print(message[6:])   # If we want to grab from between upto end

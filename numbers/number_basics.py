number_integer = 3
number_float = 3.14
number_complex = 3.14 + 3j

print(type(number_integer))
print(type(number_float))
print(type(number_complex))

# Arithmetic operators
print(3 + 2)
print(3 - 2)
print(3 * 2)
print(3 / 2)
print(3 // 2)  # floor division -> drops the decimal after division
print(3 ** 2)  # exponent -> 3 to the power of 2
print(3 % 2)   # modulus -> Gives remainder after division

num = 1
print(num + 1)
num += 1
print(num)   # Shorthand for increment

# builtin function to work with numbers
print(abs(-3))   # removes - if number is negative
print(round(3.75))
print(round(3.75, 1))   # rounds off to 1 decimal value

# comparisons
num_1 = 3
num_2 = 2
print(num_1 == num_2)
print(num_1 != num_2)
print(num_1 > num_2)
print(num_1 < num_2)
print(num_1 >= num_2)
print(num_1 <= num_2)

# casting
num_2 = float(num_2)
print(num_2)

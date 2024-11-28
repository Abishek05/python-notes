# python-notes
All Python Syntax usage guide

## Commands

1. `python --version` -> Check currently installed python version
2. `py --version`

## Common Conventions
1. Variables are all lower cases.
2. If Variables are more than 1 word then _ is used to separate them.
3. Variable names to be as descriptive as possible as what they are meant to hold.

## General Notes
1. \ (backslash) is escape character. Eg- To print the text `'Lucy's Gift'` will error out so we can use `'Lucy\'s Gift'` with escape character.
2. Alternative to the escape character we can use "" (double quotes) -> `"Lucy's Gift"`
3. Multi Line String -> `message = """This is a multi line string""`
4. Functions and methods are basically the same thing. A method is just a function that belongs to an object.
5. dir() function -> If we pass a variable into it like dir(message), it will show all of the attributes and methods that we have access to with that variable.
6. Numbers are most commonly represented with integers and floats sometimes complex number(3.14 + 3j), an integer is a whole number and a float is a decimal
7. type() function -> Builtin function where we can see the datatype of an object
8. abs() function in Number -> Builtin function to remove sign from any negative numbers. abs(-3) -> 3
9. round() function in Number -> Builtin function Round our values to nearest integer value

## Errors
1. IndexError (String index out of range)

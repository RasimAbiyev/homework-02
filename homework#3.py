# """
# Note. Use clear and descriptive variable names throughout the code.
# Make sure to add comments to explain the purpose and functionality of 
# your code.

# - String Formattings -
# A. Create a variable called 'genre'. Give it a string value.
genre = "Pop"

# B. Create a variable called 'producer'. Give it a string value.
producer = "Max Martin"

# C. Create a variable called 'song'. Give it a string value.
song = "Rock Melody"

# D. Using three Python String Formatting types, create 3 variables accordingly to the formats count,
# and make it equal to a little text (story) using all variables from Task A to C.

fstring = f"The {genre} song '{song}' was produced by {producer}."

format = "The {} song '{}' was produced by {}.".format(genre, song, producer)

percent = "The %s song '%s' was produced by %s." % (genre, song, producer)

# Print the stories
print("f-string:", fstring)
print(".format():", format)
print("%s format:", percent)

# E. Create a variable called 'firstname'. Give it an appropriate value.
firstname = "Rasim"

# F. Create a variable called 'lastname'. Give it an appropriate value.
lastname = "Abiyev"

# G. Create a variable called 'age'. Give it an appropriate value.
age = 29

# H. Create a variable called 'gender'. Give it an appropriate value.
gender = "Male"

# I. Using all of string formatting methods and variables from Task E to H,
# print as the following:

# f-string
fstring = f"My name is {firstname} {lastname}, and I am {age} years old. My gender is - {gender}."

# .format()
format = "My name is {} {}, and I am {} years old. My gender is - {}.".format(firstname, lastname, age, gender)

# %s formatting
percent = "My name is %s %s, and I am %s years old. My gender is - %s." % (firstname, lastname, age, gender)

# Print
print("f-string:", fstring)
print(".format():", format)
print("%s formatting:", percent)

# # J. Create a variable called 'language'. Make it equal 'Python'.
language = "Python"

# Using f-string to print the desired output
a = f'I love {language}. I will repeat this word 5 times: {language * 5}.'

# Print the output
print(a)
# # K. Create a variable called 'hello'. Make it equal 'Hello'.
hello = 'Hello'

# Create a variable called 'world'. Make it equal 'World'.
world = 'World'

# Using .format string-formatting method to print 'Hello World!'.
a = '{} {}!'.format(hello, world)

# Print
print(a)

# Create a variable called 'hello'. Make it equal the date of your birthday.
hello = "01.01.2001"

# Using %s string-formatting method to print the desired output
birthday = 'My birth date is %s.' % (hello)

# Print the output
print(birthday)


name = "Rasim"
age = 28
profession = "diplomat"
city_name = "Sumgait"


a = f"""
I'm {name}, {age}-year-old. I'm {profession}. I live in {city_name}.
"""

print(a)

# Variable with string value containing 4 curly brackets
placeholder_string = "{{}}{}{}{}{}"

# Additional variables of different types
variable1 = 42
variable2 = "Hello"
variable3 = 3.14
variable4 = True

# Fill the string with variables using '.format'
formatted_string = placeholder_string.format(variable1, variable2, variable3, variable4)

# Print the result
print(formatted_string)

# Variables
number1 = 10
number2 = 5

# Using f-string with math operations
result_addition = f"The sum of {number1} and {number2} is {number1 + number2}."
result_subtraction = f"The difference between {number1} and {number2} is {number1 - number2}."
result_multiplication = f"The product of {number1} and {number2} is {number1 * number2}."
result_division = f"The quotient of {number1} divided by {number2} is {number1 / number2}."

# Print the results
print(result_addition)
print(result_subtraction)
print(result_multiplication)
print(result_division)

# P. Create a variable called 'expression'. Give it any string value.
# Using a variable which you have created previously and contains 4 curly brackets
# print the 'expression's value 4 times using '.format' string-formatting method.

# Quiz:
# A. In the following code, 'Hello' is a string literal. True or false?

#     ---------------------
#     |    s = 'Hello'    | 
#     ---------------------

#     = a) True
#     b) False
#     c) It's not a string literal.
#     d) It's not a pythonic code

# B. The two strings 'Hello' and "Hello" are identical to each other. Yes or no?
#     = a) Yes
#     b) No

# C. Is there a problem in the code below? If yes, then how can we rectify it?

#     ------------------------------
#     |    s = 'Python's call!'    | 
#     ------------------------------

#     a) No
#     b) Yes, by using a backslash
#     c) Yes, bu using a multiline string
#     = d) Yes, by using either (b) or (c)

# D. How to denote a multiline string in Python?
#     a) Using ''' '''
#     b) Using """ """
#     = c) Using either (b) and (c)

# E. When used on strings, what does the * operator do?
#     a) Replicates them
#     b) Strips whitespace characters from their ends
#     = c) Raises an error
# """
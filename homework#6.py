# """
# Note. Use appropriate variable names while completing the tasks.

# - Integers -
# A. Create a variable called 'speed'. Assign any integer value between 60 and 80 to it.
speed = 70

# B. Create a variable called 'limit'. Assign any integer value between 90 and 110 to it.
limit = 100

# C. Create a variable called 'difference'. Make it equal the difference between the
# 'limit' and the 'speed' variable. Print the 'difference' variable.
difference = limit - speed
print(difference)

# D. Create a variable called 'amount'. Assign any integer value between 5 and 20 to it.
amount = 10

# E. Create a varaible called 'double_amount'. Make it equal the double value of the 'amount'
# variable.
double_amount = 2 * amount

# F. Create a varaible called 'triple_amount'. Make it equal the triple value of the 'amount'
# variable. Print these variables (amount, double_amount, triple_amount) separately.
triple_amount = 3 * amount
print(amount)
print(double_amount)
print(triple_amount)

# G. Create a variable called 'distance'. Assign any integer value between 500 and 2000 to it.
distance = 1000

# H. Create a variable called 'passed_distance'. Assign any integer value between 100 and 500 to it.
passed_distance = 250

# I. Print the difference between the 'distance' variable and the 'passed_distance' variable.
difference = distance - passed_distance
print(difference)

# J. Create a variable called 'number_one'. Give it any integer value.
number_one = 10

# K. Create a variable called 'number_two'. Give it any integer value.
number_two = 20

# L. Create a variable called 'number_three'. Make it equal to the sum of 'number_one' and 'number_two'.
# Print the value of 'number_three' variable.
number_three = number_one + number_two
print(number_three)

# M. Create a variable called 'a'. Make it equal 15.
a = 15

# N. Create a variable called 'b'. Make it equal 35.
b = 35

# O. Create a variable called 'c'. Make it equal 20.
c = 20
# P. Create a variable called 'result'. Make it equal the sum of 'a' and 'b' minus 'c'. Print its value.
result = a + b - c

# Q. Create a variable called 'my_number'. Make it equal 4.
my_number = 4

# R. Print 'my_number's raised to the third power value.
print(my_number ** 3)

# - Floats -
# A. Create a variable called 'temperature'. Make it equal any float number.
temperature = 3.7

# B. Create a variable called 'weight'. Make it equal any float number.
weight = 3.3

# C. Create a variable called 'length'. Make it equal any float number.
length = 5.5

# D. Create a variable on your own (name it appropriately). Make it equal any float number.
depth = 6.5

# E. Print all those variables from Task A to D.
print(temperature)
print(weight)
print(length)
print(depth)

# F. Create a variable called 'x'. Make it equal any float number between 1 and 2 with 2 decimal points.
x = 1.55

# G. Create a variable called 'double_x'. Make it equal double-value of 'x'
double_x = 2 * x

# H. Print all those variables from Task F to G.
print(x)
print(double_x)

# I. Make your best and create a hard task by your own using floats.
base1 = 8.5
base2 = 5.3
height = 4.2 
area = 0.5 * (base1 + base2) * height
print(area)

# - Built-in functions -
# A. Create a variable called 'long_sentence'. 
# Make it equal a long sentence. Print 'long_sentence's length.
long_sentence = "My name is Rasim"
print(len(long_sentence))

# B. Create a variable called 'accurate_number'.
# Make it equal any float number between 10 and 11 with 5 decimal points
# Print this variable.
accurate_number = 10.12345
print(accurate_number)

# C. Create a variable called 'rounded_accurate_number'.
# Make it equal the 'accurate_number's value rounded to 2 decimal points.
# Print this variable.
rounded_accurate_number = round(accurate_number, 2)
print(rounded_accurate_number)

# D. Override 'rounded_accurate_number' variable.
# Make it equal the 'accurate_number's value rounded to 3 decimal points.
# Print this variable.
rounded_accurate_number = round(accurate_number, 3)
print(rounded_accurate_number)

# E. Using 'round' method round 175233, so it gives us 175000.
print(round(175233, -3))

# - Math module -
# A. Find the 'math' module's method by its definition:
import math


# 1. The _____ method returns the square root of a number.
print(math.sqrt(16))

# 2. The _____ method returns the value of x raised to power y.
print(pow(2, 3))

# 3. The _____ method rounds a number UP to the nearest integer, if necessary, 
# and returns the result.
print(math.ceil(4.3))

# 4. The _____ method rounds a number DOWN to the nearest integer, if necessary, 
# and returns the result.
print(math.floor(4.3))

# B. Round π (Pi) to two decimal places.
print(round(math.pi, 2))

# C. The area of a square is 700 square units. Find the side of that square.
print(math.sqrt(700))

# D. One side of a rectangle is 5 units longer than other side. Find the area of
# rectangle, if the perimeter is 100 units.
side1 = 22.5
side2 = 27.5
area = side1 * side2
print(area)

# E. Round 5.7 down to the nearest integer.
print(math.floor(5.7))

# F. Round 5.7 up to the nearest integer.
print(math.ceil(5.7))

# - Expressions - 
# Simplify these expressions:
a = (5 * 5 + 5 // (5 + 5 % 5) // 5) + 5**5 + 5 - 5**0
print(a)

b = (20 + 30 * (15 - 7) // (3 + 4 % 2) + 10**2 // 5) + 2**6 + 50 - 3**1
print(b)

c = (70 - 25 + 3 * (8 + 4) // (6 + 9 % 3) + 15**2 // 7) + 4**3 + 90 - 2**4
print(c)

# - Chat GPT's Homework - 
# Task 1. Mixed Operations and Variable Naming
# Solve the following mixed arithmetic expressions, using appropriate variable names:
# a) Calculate the perimeter of a square with side length 6 units.
side_length = 6
perimeter_square = 4 * side_length
print(perimeter_square)

# b) You have $150. If you spend $47.25 and then receive $30.50, how much money do you have left?'
initial_money = 150
spent_money = 47.25
received_money = 30.5
remaining_money = initial_money - spent_money + received_money
print(remaining_money)

# c) A train is moving at a speed of 80 km/h. How far will it travel in 1.5 hours?
speed_train = 80
time_travel = 1.5
distance_traveled = speed_train * time_travel
print(distance_traveled)

# Task 2. Float Operations
# Perform the following floating-point operations and round the answers to two decimal places:
a = 4.25 + 2.68
print(round(a, 2))

b = 9.75 - 3.85
print(round(b, 2))

c = 3.5 * 1.2
print(round(c, 2))

d = 7.8 / 2.5
print(round(d, 2))

# Task 3. Accessing the Value of π (Pi)
# A. Use the math.pi attribute to access the value of π (Pi) and store it in a variable.
print(math.pi)

# B. Calculate and print the circumference of a circle with a radius of 7 units using 
# the π value from the math.pi attribute.
radius = 7
circumference = 2 * math.pi * radius
print(circumference)

# Task 4. Using 'sqrt' Method
# A. Calculate and print the square root of 16 using the math.sqrt() method.
print(math.sqrt(16))

# B. Calculate and print the square root of 25 using the math.sqrt() method.
print(math.sqrt(25))

# C. Calculate and print the square root of 10 using the math.sqrt() method.
print(math.sqrt(10))

# Task 5. Using 'pow' Method
# A. Calculate and print the result of raising 2 to the power of 5 using the math.pow() method.
print(math.pow(2, 5))

# B. Calculate and print the result of raising 3 to the power of 4 using the math.pow() method.
print(math.pow(3, 4))

# Task 6. Use the math.ceil() method to round the following numbers up to the nearest integer:
# a. 6.1
print(math.ceil(6.1))

# b. 10.9
print(math.ceil(10.9))

# c. -2.3
print(math.ceil(-2.3))

# Task 7. Use the math.floor() method to round the following numbers down to the nearest integer:
# a. 4.7
print(math.floor(4.7))

# b. 9.2
print(math.floor(9.2))

# c. -3.8
print(math.floor(-3.8))

# - Comments -
# A. One-line comment in any random three places of your code, if it's appropriate.
# Hello

# B. Multi-line comment anywhere in your code, if it's appropriate.
# """ My name is Rasim """

# Quiz:
# 1. Which of the following is a comparison operator in Python?
#     a) +
#     b) *
#     = c) ==
#     d) %

# 2. What is the result of 15.5 - 7.2 rounded to two decimal places?
#     = a) 8.3
#     b) 8.20
#     c) 8.5
#     d) 8.28

# 3. What is the result of 1.5 - 1.0 rounded to two decimal places?
#     = a) .5
#     b) 0.51
#     c) 1.0
#     d) -0.5

# 4. If 'a = 12' and 'b = 7', which expressions are True?
#     a) a < b
#     = b) a > b
#     c) a == b
#     d) a <= b
#     e) a * 7 / 12 == b

# 5. What is the value of 20/4?
#     a) 5
#     b) 4.0
#     c) 4
#     = d) 5.0
#     e) 4.5
#     f) 0.4

# 6. Which of the following are integers?
#     a) 3.14
#     = b) -15
#     c) 0.5
#     d) 1.618
#     = e) int("1")

# 7. What is the absolute value of -25?
#     = a) 25
#     b) -25
#     c) 0
#     d) 1
#     e) byte
#     g) -25.0

# 8. If 'x = 5' and 'y = 8', what is the value of x^y (x raised to power of y)?
#     a) 13
#     b) 40
#     c) 13.125
#     = d) 390625
#     e) <class 'float'>

# 9. What does the math module in Python provide?
#     a) Basic arithmetic operations for integers only.
#     b) Functions for working with complex numbers.
#     c) Advanced geometry calculations.
#     = d) A set of mathematical functions and constants.

# 10. Given the equation 3 x 8 - 5, what is the correct result?
#     = a) 19
#     b) 24
#     c) 1
#     d) 11

# 11. What is the result of 17 + 23?
#     a) 37
#     = b) 40
#     c) 12.34
#     d) 40.0
#     e) 25.67

# 12. What is the result of "17" + "23"?
#     a) "37"
#     b) "40"
#     c) "12.34"
#     = d) "1723"
#     e) "17 + 23"
# """
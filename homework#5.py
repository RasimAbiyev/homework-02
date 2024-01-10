# # """
# # - I/O -
# # Warning! 1. You should set appropriate variable names each time when
# # you create a variable. 2. You should ask users appropriate questions.
# # 3. Pay attention to the question style, try to decorate it.

# # A. Write a program that asks user for his/her name.
# # Print the name in capitalized form, so if the user
# # types in 'aysel', we should see 'Aysel' on the console.
her_name = input()
print(her_name.capitalize())

# # B. Ask user for their age. Subtract this age from 50.
her_age = int(input())
result = 50 - her_age
print(result)

# # C. Ask user for their address, favorite color, car brand.
# # Using multi-line string formatting print this values using it
# # in a sentence.
address = input()
color = input()
brand = input()
print(f"""{address}, {color}, {brand}""")

# # D. Write a calculator that plusses user's inputted numbers.
num = int(input())
num1 = int(input())
print(num + num1)

# # E. Write a calculator that subtracts user's inputted numbers.
num = int(input())
num1 = int(input())
print(num - num1)

# # F. Write a calculator that multiplies user's inputted numbers.
num = int(input())
num1 = int(input())
print(num * num1)

# # G. Write a calculator that divides user's inputted numbers.
num = int(input())
num1 = int(input())
print(num / num1)

# # H. Ask user for 3 different numbers. Multiply first two numbers
# # and then divide the result by the third inputted number.
num = int(input())
num1 = int(input())
num2 = int(input())
print((num + num1) / num2)

# # I. Write a program that prints the length of user's full name.
name = input()
print(len(name))

# J. Write a program that asks user for some Float number. This program
# soon will round this float number. Additionally, we need to ask for
# how many decimal digits user want to round it to. Print its rounded
# value.
num = float(input())
print(round(num))

# K. Write a program that asks for 2 numbers. 1st number is the main
# number, and the 2nd number is for the power the user wants the 1st
# number to raise to. So if the 1st number is 16, and the 2nd is 2,
# we should see 256 on the console.
num = int(input())
num1 = int(input())
print(pow(num, num1))

# L. Write a program that asks user for any single word. Then ask for
# any number, because we will call String's 'center' method and give
# it the number user inputted.
name = input()
num = int(input())
print(name.center(num))

# M. Write a program that asks 'How many times should the program
# type "Python" word?'. Print the 'Python' word given number times.
# For example, if user gives us the 5 number, we should see on console:
# PythonPythonPythonPythonPython
name = input()
print(name * 5)

# N. Write a program that asks user for any sentence. The program should
# replace all characters in the sentence with its capitalized form.
# Given "I love the Python", the program should give us:
# I LOVE THE PYTHON
sentence = input()
print(sentence.upper())

# O. Write a program that asks user for any sentence. The program should
# replace all 'a' character in the sentence with 'o'. Given "Today is a
# great day!", the program should give us:
# Todoy is o greot doy!
sentence = input()
print(sentence.replace("a", "o"))

# P. Write a program that asks user for any input. The program should
# print 'True' if all characters in the input are lower characters.
name = input()
print(name.islower())

# Q. Write a program that asks user for any input. The program should
# print 'True' if all characters in the input are digits.
name = input()
print(name.isdigit())

# R. Write a program that asks user for any phrase. The program should also
# ask for the amount the phrase will be printed. Depending on that amount print
# the user's phrase to terminal output.
name = input()
print(f"{name}\n{name}\n{name}")

# S. Write a program that asks user for any amount. Depending on that amount you
# should print the stars before and after the 'Hello world' phrase. Example:
# (Amount is 3)
# *** Hello world ***
name = input()
amount = "*" * 3
print(f"{amount} {name} {amount}")

# - Chat GPT's Homework -
# Task 1. Create a Python program that greets the user and asks for their name. 
# Use the input() function to receive the user's input and then print a personalized greeting.
user_name = input()
print(user_name)

# Task 2. Extend the program from Task 1 to ask the user for their birth year and 
# calculate their age. Display a message that includes their name and age.
year = int(input())
year1 = int(input())
print(year -  year1)

# Task 3. Write a program that takes two numbers as input from the user and performs 
# the following math operations:
# A. Addition
num = int(input())
num1 = int(input())
print(num + num1)

# # B. Subtraction
print(num - num1)

# # C. Multiplication
print(num * num1)

# # D. Division
print(num / num1)

# Task 4. Create a program that calculates the area of a triangle.
# Ask the user for the necessary inputs for calculations. 
base = int(input())
height = int(input())
area = 0,5 * base * height
area1 = 1/2 * base * height
print(area)
print(area1)
print(1/2 * base * height)
print(0,5 * base * height)

# Task 5. Create a program that calculates the area of a rectangle.
# Ask the user for the necessary inputs for calculations.
length = int(input())
width = int(input())
print(length * width)

# Task 6. Create a program that calculates the area of a square.
# Ask the user for the necessary inputs for calculations.
side = int(input())
print(side ** 2)

# Task 7 (Extra!). For an extra challenge, implement a unit conversion feature. 
# Ask the user for a distance in meters and convert it to feet and inches. 
# There are approximately 3.28084 feet in a meter and 39.3701 inches in a meter. 
# Display the converted distances.
feet_meter = 3.28084
inches_meter = 39.3701
distance_meters = int(input())
distance_inches = int(input())
distance_feet = distance_meters * feet_meter
distance_inches = distance_inches * inches_meter
print(distance_meters)
print(f"distance_feet >> {distance_feet}")
print(f"distance_inches >> {distance_inches}")

# Quiz:
# 1. Which of the following functions is used to convert a value to an integer in Python?
#     = a) int()
#     b) float()
#     c) bool()
#     d) str()

# 2. When using the input() function in Python, what data type is the input value 
# stored as by default?
#     a) int
#     b) float
#     = c) str
#     d) input

# 3. You want to find out how many characters are in a user-inputted sentence. 
# Which Python function would you use?
#     a) length()
#     b) count()
#     = c) len()
#     d) uzunluq()

# 4. If a user enters "3.14159" as input using the input() function, how can you 
# convert it to a floating-point number?
#     = a) float(input())
#     b) input().to_float()
#     c) input().convert(float)

# 5. If a user enters "5.7" as input using the input() function and you use 
# int(input()) for conversion, what will happen?
#     = a) An error will occur since int() cannot handle decimal values.
#     b) The value will be converted to the nearest integer, resulting in 6.
#     c) The decimal part will be truncated, resulting in 5.

# 6. You want to display the length of a user-inputted string "Hello, World!" with a 
# descriptive message. Which option achieves this?
#     = a) print("The length of the input is:", len(input()))
#     b) print("The length of the input is: " + len(input()))
#     c) print("The length of the input is:", + len(input())

# 7. What happens if a user enters "42" as input and you use float(input()) for 
# conversion?
#     a) An error occurs because float() cannot convert integer strings.
#     = b) The value is converted to the floating-point number 42.0.
#     c) The value remains unchanged as a string.

# 8. To style the user prompt and concatenate it with a variable, which option is correct?
#     a) input("Enter your name: " + name)
#     = b) input("Enter your name: ") + name
#     c) input("Enter your name: ") .format(name)
# """

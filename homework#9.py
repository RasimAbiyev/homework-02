# """
# Note. You should use indexing, negative indexing, slicing method,
# mathematical operations and other techniques to accomplish tasks.

# - Lists -
# A. Create a list containing minimum seven different colors.
color = ["brown", "yellow", "white", "black", "green", "blue", "red"]

# B. Create a list containing minimum five different countries.
country = ["Azerbaijan", "Turkey", "Italy", "Germany", "America"]

# C. Create a list containing three string values and two integer values.
my_list = ["apple", "banana", "orange", 10, 20]

# D. Create a list containing all continents of the world.
continent = ["Europe", "Asia", "Africa", "Antartica", "North America", "South America"]

# E. Create a list containing minimum four car brands.
car_brand = ["Honda", "Toyota", "Mitsubishi", "Ford"]

# F. Create a list containing four different data types of Python.
data_type = [42, "Hello", 3.14, True]

# G. Create a list containing only negative even numbers from -2 to -12.
negative = [-2, -4, -6, -8, -10, -12]

# H. Create a list containing only positive even numbers from 0 to 12.
positive = [2, 4, 6, 8, 10, 12]

# I. Combine lists from Task G and H.
combine = negative + positive

# J. Create a list containing minimum six students' names. Print the first
# student's name.
name = ["Kamran", "Elnur", "Eldar", "Kamal", "Telman", "Adil"]
print(name[0])

# K. Create a list containing three different integers. Print the integer
# at position two.
num = [1, 2, 3]
print(num[1])

# L. Print the last element of Task D's list.
print(continent[-1])

# M. Print the last 2 elements of Task A's list. You can use slicing
# method only once. Separately printing those elements will not be accepted.
print(color[-2:])

# N. Given the following list:
three = [3, 3, 3]

# Create a new list containing the triple value of that list.
triple_value = [value * 3 for value in three]

# O. Create any nested list. Print any value from the inner list and the whole
# inner list.
nested_list = [[1, 2, 3], ['a', 'b', 'c'], [10, 20, 30]]
print(nested_list[1][2])
print(nested_list[1])

# P. Change the value of the color at position six of the list from Task A.
color[5] = "pink"
print(color)

# Q. From Task B's list print all countries except the first two.
print(country[2:])

# R. Create two new lists containing the double value of the list from Task F 
# using 2 different mathematical operations (methods).
double_value_1 = [value * 2 for value in data_type]
double_value_2 = [value + value for value in data_type]

# S. From the following list change the value of the last element to "Bob":
friends = ["Kevin", "Karen", "Jim", "Carry"]
friends[-1] = "Bob"

# T. Create an empty list.
empty_list = []

# - Interview Question -
# A. Reverse a list with slicing method.
original_list = [1, 2, 3, 4, 5]
reversed_list = original_list[::-1]

# Bonus:
# A. Print the whole list from previous tasks using the slicing method.
whole_list = car_brand[:]
print(whole_list)

# B. Print the length of any list from previous tasks.
print(len(my_list))
# """
# """
# Note. Add the following list at the top of your code. You will use this list
# during the homework in certain tasks:
fruits = ["Apple", "Banana", "Orange", "Grape", "Strawberry", "Kiwi", "Cherry"]

# Also print the list's modification versions to see the difference.
# - List Methods -
# A. Make up a formula with built-in python 'len' method that finds helps 
# to get the last element from the 'fruits' list.
fruits[len(fruits) - 1]

# B. Add any two fruits to the 'fruits' list.
fruits.append("Ananas")
fruits.append("Mango")

# C. Remove third fruit so you can assign it to a variable.
fruits.pop(2)

# D. Add a fruit to the 'fruits' list twice, and then print the amount of 
# this fruit
# in the 'fruits' list.
fruits.append("Banana")
fruits.append("Banana")
fruits.count("Banana")

# E. Find the index of 'Grape' object in the 'fruits' list.
fruits.index("Grape")

# F. Add 'Avocado' to the 'fruits' list at position four.
fruits.insert(3, "Avocado")

# G. Remove third fruit without getting the removed fruit.
fruits.pop(2)

# H. Remove a fruit at position one.
fruits.pop(0)

# I. Add 'Blackberry' to the end of the 'fruits' list. Remove it using 'pop' 
# method
# by finding its positive index.
fruits.append("Blackberry")
print(fruits.index("Blackberry"))
fruits.pop(7)

# J. Reverse the 'fruits' list with two different methods. Each time print 
# the reversed
# list.
fruits.reverse()
reverse = fruits[::-1]

# K. Sort alphabetically the 'fruits' list. Print the sorted version of the 
# list.
fruits.sort()

# L. Suppose you have the following list:
fruits = ["Apple", "Banana", "Orange", "Grape", "Strawberry", "Kiwi", "Cherry"]
new_fruits = ["Papaya", "Lime", "Lemon", "Peach"]

# Extend the 'fruits' list with the new list.
fruits.extend(new_fruits)

# M. Make a copy of the 'fruits' list. Remove the last three fruits. Print
# both of the
# lists ('fruits' and the modified copied version).
fruits = ["Apple", "Banana", "Orange", "Grape", "Strawberry", "Kiwi", "Cherry"]
print(fruits)
name = fruits.copy()
del name[-3:]
print(name)

# N. Create a variable named 'occurrence'. Make it equal True if the 
# 'Papaya' is in the
# 'fruits' list, otherwise False.
occurence = "Papaya" in fruits
print(occurence)

# O. Clear the 'fruits' list.
fruits.clear()
print(fruits)

# - Variables -
# A. Suppose you have the following variables:
x = 60
y = 70

# You need to swap these variables values in one line of code.
x,y = y, x

# - ChatGPT's homework (List Methods) -
# 1. Append and Extend:
# a. Write a Python program that creates an empty list and then appends 
# the following elements to it: 10, 20, 30, 40, and 50. Print the list 
# after each append operation.
empty_list = []
empty_list.append(10)
print(empty_list)
empty_list.append(20)
print(empty_list)
empty_list.append(30)
print(empty_list)
empty_list.append(40)
print(empty_list)
empty_list.append(50)
print(empty_list)

# b. Create a second list containing elements [60, 70, 80]. Extend the 
# first list using this second list and print the updated list.
num = [60, 70, 80]
empty_list.extend(num)
print(empty_list)

# 2. Insert and Remove:
# a. Write a Python program that creates a list containing the following 

elements = ['apple', 'banana', 'orange', 'grape', 'apple', 'kiwi']

# b. Use the 'insert' method to add 'pear' between 'banana' and 'orange' 
# in the list. Print the updated list.
elements.insert(2, 'pear')
print(elements)

# c. Use the 'remove' method to remove the first occurrence of 'apple' from 
# the list. Print the updated list.
elements.remove('apple')
print(elements)

# 3. Count and Index:
# a. Create a list containing the following elements:
num = [2, 4, 6, 8, 4, 10, 4, 12, 14]

# b. Use the 'count' method to find how many times the number 4 appears in the 
# list and print the count.
a = num.count(4)
print(a)

# c. Use the 'index' method to find the index of the first occurrence of 4 in 
# the list and print the index.
b = num.index(4)
print(b)

# 4. Sort and Reverse:
# a. Create a list containing the following integers in random order:
int = [45, 23, 78, 12, 98, 56]

# b. Use the 'sort' method to sort the list in ascending order and print the 
# sorted list.
int.sort()
print(int)

# c. Use the 'reverse' method to reverse the sorted list and print the reversed 
# list.
int.reverse()
print(int)

# 5. Slice and Concatenate:
# a. Create a list containing the following elements:
color = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']

# b. Use slicing to extract a new list that contains only the first three 
# colors. Print the new list.
print(color[:3])

# c. Use slicing again to extract a new list that contains the last three
# colors. Print the new list.
print(color[-3:])

# d. Concatenate the two sliced lists and print the final combined list.
print(color[:3] + color[-3:])
# """
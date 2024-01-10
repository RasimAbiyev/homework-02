# """
# - Lists -
# A. Create an empty list and add 5 user-input integers to it.
empty_list = [ ]
new_empty1 = int(input())
new_empty2 = int(input())
new_empty3 = int(input())
new_empty4 = int(input())
new_empty5 = int(input())
empty_list.append(new_empty1)
empty_list.append(new_empty2)
empty_list.append(new_empty3)
empty_list.append(new_empty4)
empty_list.append(new_empty5)
print(empty_list)

# B. Take a list of integers as input and print the sum of all the elements in the list.
my_list = [ ]
my_list1 = int(input())
my_list2 = int(input())
my_list3 = int(input())
my_list4 = int(input())
my_list5 = int(input())
my_list.append(my_list1)
my_list.append(my_list2)
my_list.append(my_list3)
my_list.append(my_list4)
my_list.append(my_list5)
print(sum(my_list))

# C. Ask the user for a sentence and store each word as an element in a list.
user_sentence = input()
word_list = user_sentence.split()
print(word_list)

# D. Write a program that asks user for six countries. The program should create a list of
# those countries and ask for three countries to delete from the list. Make the program
# user-friendly, and print each time the content of a list to show the user which countries
# are in a list.
countries =  ["Azerbaijan", "Turkey", "Ukrain", "England", "Russia", "Italy"]
countries.remove("Turkey")
countries.remove("Azerbaijan")
countries.remove("Ukrain")
print(countries)

# E. Which list method makes any list look the same. The lists are the same if its content,
# elements and all other properties are the same.
list1 = [4, 1, 3]
list2 = [4, 1, 3]
list1.sort()
list2.sort()
print(list1 == list2)

# F. Create an empty list and print its length.
# Write a function that accepts a list of names and returns the name with the longest length.
empty_list = [ ]
print(len(empty_list))
name_list = ["Bob", "Charlie", "Alice", "David", "Eva"]
print(max(name_list, key=len))

# G. Ask the user for a list of integers and find the second-largest number in the list.
num = int(input())
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = [num, num1, num2, num3]
num4.sort()
print(num4[-2])

# H. Ask the user for a list of integers and find the mean value of that list.
# Get list of integers from the user
num = int(input())
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = [num, num1, num2, num3]
print(sum(num4) / len(num4))

# I. Ask the user for a list of integers and find the third-smallest number in the list.
num = int(input())
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = [num, num1, num2, num3]
num4.sort()
print(num4[2])

# J. Write a program that asks the user for three colors separated by spaces. The
# program should print all those colors using comma (you should use string 'join' method). 
# For example:
# Your colors are red, blue, white.
color = input()
print(", ".join(color.split()))

# K. Write a program that asks the user for four capital cities separated by spaces.
# The program should print all those cities the following structure:
# There are many capital cities in the world. For example, Baku, Moscow and Kyiv.
# You should follow all instructions, and not make changes to the structure of final sentence.
capital_city1 = input()
capital_city2 = input()
capital_city3 = input()
capital_city4 = input()
print(f"{capital_city1}, {capital_city2}, {capital_city3}, and {capital_city4}.")
capital_city = input()
print(capital_city)

# L. Take a list of strings as input and sort it in alphabetical order.
string = input()
str = string.split()
str.sort()
print(str)

# M. Take a list of numeric values as input and sort it in descending order.
num = int(input())
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = [num, num1, num2, num3]
num4.sort(reverse=True)
print(num4)

# N. Remove duplicates from a list entered by the user while preserving the original order.
user_input = input()
original_list = user_input.split()
original_order = list(set(original_list))
print(list(set(original_list)))

# O. Write a program that accepts two lists and concatenates them into a single list.
# The first list is a list of fruits, the second is a list of vegetables.
fruit = ["mango", "kiwi", "lemon", "apple", "banana"]
vegetable = ["potato", "cabbage", "carrot", "onion", "cucumber"]
fruit = input()
fruit = fruit.split()
vegetable = input()
vegetable = vegetable.split()
combine = fruit + vegetable
print(combine)

# P. Write a program that prints 'True' if there is at least one item in a 'my_list' list.
my_list = [1, 2, 3, 4, 5]
print(bool(my_list))

# - List Comprehension -
# Suppose you have the following lists:
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
letters = ['p', 'y', 't', 'h', 'o', 'n']
times = [1, 2, 3, 4, 5]

# A. Create a list containing raised to power two values of 'digits' list.
power = [x ** 2 for x in digits]
print(power)


# B. Create a list containing capitalized version of letter values of 'letters' list.
capitalize = [letter.capitalize() for letter in letters]
print(capitalize)

# C. Create a list containing the 'Comprehension' string value the amount of 'times'
# list's length time.
comprehension = ["Comprehension" * count for count in times]
print(comprehension)

# D. Create a list containing 5 random integers between -5 and 5. find the second-smallest 
# number in the list. The program should print 'True' if that number is negative, and 'False'
# otherwise.
import random

ran = [random.randint(-5, 5) for _ in range(5)]
ran.sort()
ran[1]
print(ran[1] < 0)

# E. Create a list of 10 random numbers and find the maximum and minimum values.
ran = [random.random() for _ in range(10)]
print(max(ran))
print(min(ran))

# - Comments -
# A. One-line comment, if it's appropriate.
# Hello

# B. Multi-line comment, if it's appropriate.
# """
# My name is Rasim
# """

# - Chat GPT's Homework -
# A. Create a list of colors and write a function that duplicates each color in the 
# list. For example, if the list contains "red," it should become ["red", "red"]. 
# Print the modified list.
colors = ["red", "blue", "green", "yellow", "orange"]
duplicate = [color for color in colors for _ in range(2)]
print(duplicate)

# B. How many methods do you know to create an empty list in Python?
empty_list = [ ]
# There is a lot of method. Example:
print(empty_list[:])
empty_list1 = list()
num_list = [1, 2, 3]
print(num_list[0:0])
num_list.clear()
empty_list2 = [*()]
empty_list.extend([])

# C. Which list method is used to add an element to the end of a list?
my_list = [10, 20, 30, 40]
my_list.append(50)

# D. Write a Python code snippet to access the third element in a list named my_list.
my_list = [10, 20, 30, 40, 50]
my_list[2]

# E. Which list method is used to remove the last element from a list?
my_list = [10, 20, 30, 40, 50]
my_list.pop()

# F. What list method is used to insert an element at a specific position?
my_list = [10, 20, 40 ,50]
my_list.insert(2, 30)

# G. Write Python code to reverse a list called my_list in-place.
my_list = [10, 20, 30, 40, 50]
my_list.reverse()

# H. How can you create a shallow copy of a list in Python? 
my_list = [10, 20, 30, 40, 50]
print(my_list.copy())

# I. Which list method is used to count the number of occurrences of a specific element in a list?
my_list = [10, 20, 30, 10, 40, 10, 50]
print(my_list.count(10))

# J. Write a Python code snippet to concatenate two lists, list1 and list2.
my_list1 = [1, 2, 3, 4, 5]
my_list2 = [10, 20, 30, 40, 50]
print(my_list1 + my_list2)


# K. What list method can be used to sort a list in ascending order?
my_list = [2, 6, 4, 1, 7, 9, 5, 3, 8]
my_list.sort()
print(my_list)

# L. Write Python code to remove the first occurrence of an element 'x' from a list.
my_list = [10, 20, 30, 40, 50]
my_list.remove(10)

# M. Explain the difference between append() and extend() methods when adding elements to a list.
# The append() method is used to add a single element to the end of a list.
# The extend() method is used to add elements from an iterable (e.g., a list, tuple, or string) to the end of a list.

# N. Which list method can be used to remove all elements from a list? 
my_list = [1, 2, 3, 4, 5]
my_list.clear()

# O. Write Python code to find the index of the first occurrence of an element 'x' in a list.
my_list = [10, 20, 30, 40, 50]
print(my_list.index(20))

# P. What list method can be used to remove and return an element from a specific index in a list?
my_list = [10, 20, 30, 40 ,50]
remove = my_list.pop(2)
print(remove)
print(my_list)

# Quiz.
# 1. Which method is used to add an element to the end of a list in Python?
#     a) add()
#     b) insert()
#     c) extend()
#     = d) append()

# 2. What is the purpose of the insert() method for lists in Python?
#     a) Remove an element from a list.
#     b) Add an element to the beginning of a list.
#     = c) Add an element at a specific index in the list.
#     d) Replace an element at a specific index in the list.

# 3. Which list method is used to remove and return the last element of a list?
#     = a) pop()
#     b) remove()
#     c) delete()
#     d) discard()    

# 4. What does the extend() method do when used on a list in Python?
#     a) Adds an element to the beginning of the list.
#     = b) Adds a new list as elements to the existing list.
#     c) Removes the last element from the list.
#     d) Sorts the list in ascending order.

# 5. Which list method is used to reverse the order of elements in a list in Python?
#     = a) reverse()
#     b) flip()
#     c) backwards()
#     d) revert()

# 6. What does the sort() method do when used on a list in Python?
#     a) Reverses the order of elements in the list.
#     b) Removes all elements from the list.
#     = c) Sorts the list in ascending order.
#     d) Sorts the list in descending order.

# 7. Which method is used to find the index of the first occurrence of an element in a list?
#     = a) index()
#     b) find()
#     c) search()
#     d) lookup()

# 8. What is the purpose of the pop() method when used on a list in Python?
#     a) Adds an element to the end of the list.
#     = b) Removes and returns the last element of the list.
#     c) Removes the first element of the list.
#     d) Inserts an element at a specific index in the list.

# 9. How can you count the number of occurrences of a specific element in a list?
#     = a) Use the count() method.
#     b) Use the occurrences() method.
#     c) Use the find_count() method.
#     d) Use the search_count() method.

# 10. How can you check if a list is empty in Python?
#     a) Use the empty() method.
#     b) Use the is_empty() method.
#     = c) Use the len() function and check if it's equal to zero.
#     d) Use the has_elements() method.

# 11. Which method is used to copy the elements of one list to another in Python?
#     = a) copy()
#     b) duplicate()
#     c) clone()
#     d) replicate()

# 12. How do you remove an element by index from a list in Python?
#     a) Use the remove() method with the index as an argument.
#     = b) Use the pop() method with the index as an argument.
#     c) Use the delete() method with the index as an argument.
#     d) Use the discard() method with the index as an argument.

# 13. What does the len() method do when applied to a list?
#     a) Returns the maximum value in the list
#     b) Returns the minimum value in the list
#     = c) Returns the number of elements in the list
#     d) Returns the sum of all elements in the list

# 14. Given the following list, what is the output of min(my_list)?
my_list = [0, 2, 4, 1, 5]
result = min(my_list)

#     = a) 0
#     b) 1
#     c) 4
#     d) 5

# 15. Given the following list, what is the output of max(my_list)?
my_list = [0, 2, 4, 1, 5]

#     a) 0
#     b) 1
#     c) 4
#     = d) 5

# 16. Which list method can be used to find the number of occurrences 
# of a specific element in a list?
#     = a) count()
#     b) len()
#     c) sum()
#     d) max()

# 17. What is the output of the following code snippet?
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)

#     a) [1, 2, 3, 4, 5]
#     = b) [5, 4, 3, 2, 1]
#     c) [1, 2, 3, 4]
#     d) [5, 4, 3, 2]

# 18. What is the output of the following code snippet? 
my_list = [1, 2, 3] 
my_list.insert(1, 4) 
print(my_list)

#     a) [1, 2, 3] 
#     = b) [1, 4, 2, 3] 
#     c) [4, 1, 2, 3] 
#     d) [1, 2, 4, 3] 

# 19. Which method is used to remove all elements from a list? 
#     = a) clear() 
#     b) remove_all() 
#     c) delete_all() 
#     d) reset() 

# 20. What is the output of the following code snippet? 
my_list = [1, 2, 3, 4, 5] 
result = sum(my_list) 
print(result)

#     = a) 15 
#     b) [1, 2, 3, 4, 5] 
#     c) [5, 4, 3, 2, 1] 
#     d) 10 

# 21. What is the output of the following code snippet? 
my_list = [1, 2, 3, 4, 5] 
result = my_list.index(3) 
print(result)

#     a) 0 
#     b) 1 
#     = c) 2 
#     d) 3
# """
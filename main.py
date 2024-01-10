# # # # Define variables
# # # hello = "Hello"
# # # world = "World"

# Which list method is used to remove the last element from a list?
# There is a lot of method. Example:
# pop(), [:-1], del, remove[-1], pop(-1)

# Which list method is used to add an element to the end of a list?
# There is a lot of method. Example:
# append(), insert(), extend(), +=

# What list method is used to insert an element at a specific position?
# I know one method. Example:
# [2:2]

# # # # Use format method
# # # print("{0} {1}!".format(hello, world))

# # # # Variable with string value containing 4 curly brackets
# # # placeholder_string = "{}{}{}{}{}"

# # # # Print the string
# # # print(placeholder_string)

# # # # Variables
# # # curly_brackets = "{ }{ }{ }{ }"
# # # variable1 = 42
# # # variable2 = "Hello"
# # # variable3 = 3.14
# # # variable4 = True

# # # # Fill the string with variables
# # # formatted_string = curly_brackets.format(variable1, variable2, variable3, variable4)

# # # # Print the result
# # # print(formatted_string)

# # # # Variables
# # # curly_brackets = "{}{}{}{}{}"
# # # variable1 = 42
# # # variable2 = "Hello"
# # # variable3 = 3.14
# # # variable4 = True

# # # # Fill the string with variables
# # # formatted_string = curly_brackets.format(variable1, variable2, variable3, variable4)

# # # # Print the result
# # # print(formatted_string)

# # # Variable with string value containing 4 curly brackets
# placeholder_string = "{},{},{},{}"

# # Additional variables of different types
# variable1 = 42
# variable2 = "Hello"
# variable3 = 3.14
# variable4 = True

# # # Fill the string with variables using '.format'
# formatted_string = placeholder_string.format(variable1, variable2, variable3, variable4)

# print(formatted_string)



# placeholder_string1 = "{}\n,{}\n,{}\n,{}"


# # Additional variables of different types
# variable1 = 42
# variable2 = "Hello"
# variable3 = 3.14
# variable4 = True

# # # Fill the string with variables using '.format'
# formatted_string1 = placeholder_string1.format(variable1, variable2, variable3, variable4)


# print(formatted_string1)


# # # Print the result
# # print(formatted_string)

# # expression_one = "Salam"

# # # placeholder_string = "{}"
# # string_one = "{}".format(expression_one)
# # string_two = "{}".format(expression_two)
# # string_three = "{}".format(expression_three)
# # string_four = "{}".format(expression_four)
# # print(string_one)
# # print(string_two)
# # print(string_three)
# # print(string_four)

# expression = "Salam"
# template = "{}{}{}{}"
# print(template.format(expression, expression, expression, expression))

# name = "Rasim"
# print(f"{name}")

# amount_input = input("Reqem daxil et: ")
# name = "Mark"
# name = "Rasim"
# name = "Elnur"
# name = "Farhad"
# print(name)

# my_tuple = ('apple', 'banana', 'orange', 5, 10)

# # Print the last two elements using slicing
# print("Last two elements:", my_tuple[-2:])

# print(2 + "2")
# print("4" * 2)

# HHSHHSHS_SSHSHSH = "MarkHGFHJJJDSSD"
# print(HHSHHSHS_SSHSHSH)

# def remove_item_from_set(item, my_set):
#     if item in my_set:
#         my_set.remove(item)
#         print(f"{item} removed from the set.")
#     else:
#         print(f"{item} not found in the set.")

# Example usage:
# ages = {25, 30, 35, 40, 45}

# print("Original set:", ages)

# ages.remove(int(input("Enter the item to remove: ")))

# # remove_item_from_set(item_to_remove, ages)

# print("Updated set:", ages)

# ages = {12, 14, 16, 18, 20, 22, 24, 26}

# # Remove 18 from the set if it is present
# # if 18 in ages:
# ages.remove(18)

# print(ages)

# my_set = {1, 2, 3, 4}
# my_set.discard(3)
# my_set.discard(5)
# print(my_set)
# my_set = {1, 2, 3, 4}
# my_set.remove(3)  # Removes 3 from the set
# my_set.remove(5)  # Raises KeyError: 5 not in set
# print(my_set)

# Create an empty list called shopping_cart
# shopping_cart = []

# 1. Add three items to the shopping cart
# shopping_cart.append("Apples")
# shopping_cart.append("Milk")
# shopping_cart.append("Bread")

# # Display the shopping cart after adding items
# print("Shopping Cart after adding items:", shopping_cart)

# # 2. Remove one item from the shopping cart
# item_to_remove = "Milk"
# if item_to_remove in shopping_cart:
#     shopping_cart.remove(item_to_remove)
#     print(f"Removed {item_to_remove} from the shopping cart.")
# else:
#     print(f"{item_to_remove} not found in the shopping cart.")

# # Display the shopping cart after removing an item
# print("Shopping Cart after removing an item:", shopping_cart)

# 3. Modify one of the items in the shopping cart
# item_to_modify = "Apples"
# if item_to_modify in shopping_cart:
#     index_to_modify = shopping_cart.index(item_to_modify)
#     shopping_cart[index_to_modify] = "Oranges"
#     print(f"Modified {item_to_modify} to Oranges in the shopping cart.")
# else:
#     print(f"{item_to_modify} not found in the shopping cart.")

# # Display the shopping cart after modifying an item
# print("Shopping Cart after modifying an item:", shopping_cart)

# s = {1, 3, 7, 6, 5}
# s.discard(4)
# print(s)

# print(min(max(False,-3,-4),2,7))
# print(max(min(False, False),1, True))

# # we can also build lists, first start with an empty one
# elements = []

# # then use the range function to do 0 to 5 counts
# for i in range(0, 6):
#  print(f"Adding {i} to the list.")
# # append is a function that lists understand
# elements.append(i)

# # now we can print them out too
# for i in elements:
#  print(f"Element was: {i}")

# the_count = [1, 2, 3, 4, 5]
# fruits = ['apples', 'oranges', 'pears', 'apricots']
# change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# # this first kind of for-loop goes through a list
# for number in the_count:
#     print("This is count %d" % number)

# # same as above
# for fruit in fruits:
#     print("A fruit of type: %s" % fruit)

# # also we can go through mixed lists too
# # notice we have to use %r since we don't know what's in it
# for i in change:
#     print("I got %r" % i)

# # we can also build lists, first start with an empty one
# elements = []

# # then use the range function to do 0 to 5 counts
# for i in range(0, 6):
#     print("Adding %d to the list." % i)
#     # append is a function that lists understand
#     elements.append(i)

# # now we can print them out too
# for i in elements:
#     print("Element was: %d" % i)

# the_count = [1, 2, 3, 4, 5]
# fruits = ['apples', 'oranges', 'pears', 'apricots']
# change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# # this first kind of for-loop goes through a list
# for number in the_count:
#     print("This is the_count %d" % number)

# # same as above
# for fruit in fruits:
#     print("A fruit of type: %s" % fruit)

# # also we can go through mixed lists too
# # notice we have to use %r since we don't know what's in it 
# for i in change:
#     print("I got %r" % i)

# # we can also build lists, first start with an empty one
# elements = []

# # then use the range function to do 0 to 5 counts
# for i in range(0, 6):
#     print("Adding %d to the list." % i)
#     # append is a function that lists understand
#     elements.append(i)

# # now we can print them out too
# for i in elements:
#     print("Element was: %d" % i)

# # we can also build lists, first start with an empty one
# elements = []

# # then use the range function to do 0 to 5 counts
# for i in range(0, 6):
#     print(f"Adding {i} to the list.")
# # append is a function that lists understand
# elements.append(i)

# # now we can print them out too
# for i in elements:
#     print(f"Element was: {i}")

# # we can also build lists, first start with an empty one
# elements = []

# # then use the range function to do 0 to 5 counts
# for i in range(0, 6):
#  print(f"Adding {i} to the list.")
# # append is a function that lists understand
# elements.append(i)

# # now we can print them out too
# for i in elements:
#  print(f"Element was: {i}")

# a = "Hello"
# b = 5
# a, b = b, a
# print(a, b)

# str_one = input(">>>> ")
# num_two = input(">>>> ")
# num_three = str_one + num_two 
# print(f"{str_one} + {num_two} = {num_three}")

# str_one = input("> ")
# str_two = input("> ")
# str_three = str_one + str_two 
# print(f"{str_one} + {str_two} = {str_three}")

# def string_calculator(str1, str2):
#     result = str1 + str2
#     return result

# # Get input from the user
# input_str1 = input("Enter the first string: ")
# input_str2 = input("Enter the second string: ")

# # Call the string calculator function and print the result
# result_string = string_calculator(input_str1, input_str2)
# print(f"The result of adding {input_str1} and {input_str2} is: '{result_string}'")

# str_one = input("> ")
# str_two = input("> ")
# str_three = str_one + str_two 
# print(f"{str_one} + {str_two} = '{str_three}'")

# num_one = input(">>> ")
# num_two = input(">>> ")
# num_three = num_one + num_two 
# print(num_three)

# import string
# import random

# def generate_password(length=-1):
#     # Define character sets for password
#     lowercase_letters = string.ascii_lowercase
#     uppercase_letters = string.ascii_uppercase
#     digits = string.digits
#     special_characters = string.punctuation

#     # Combine character sets
#     all_characters = lowercase_letters + uppercase_letters + digits + special_characters

#     # Generate a random password
#     password = ''.join(random.choice(all_characters) for _ in range(length))

#     return password

# # Get user input for password length
# password_length = int(input("Enter the desired password length: "))

# # Generate and print the password
# generated_password = generate_password(password_length)
# print(f"Generated Password: {generated_password}")

# import string
# import random

# def generate_password(length):
#     # Combine lowercase and uppercase letters
#     letters = string.ascii_lowercase + string.ascii_uppercase
#     password = ''.join(random.choice(letters) for _ in range(length))
#     return password

# # Example: Generate a password with a length of 10
# password = generate_password(10)
# print(password)

# import getpass

# password = getpass.getpass("Enter your password: ")
# print("Password entered:", password)
# import math
# number = 57_999.99
# print(math.floor(number))

# number = 0.0592481
# print(math.ceil(number))

# num = 5.5 ** 5
# print(num)

# x = None
# y = None
# print(x == y)
# print(x is y)

# import random

# random_integer = random.randint(5, 10)
# print(random_integer)

# random_float = random.random()
# print("Random float between 0 and 1 (exclusive):", random_float)
# import math
# # print(math.pi)

# x = 7.6
# print(math.ceil(x))
# import random
# for _ in range(5):
#     print(random.randint(50, 100))

# num = float(input())
# print(math.sqrt(num))

# original_string = "This is a string to be reversed."
# reversed_string = original_string[::-1]
# print(reversed_string)

# data_type = [42, "Hello", 3.14, True]
# mixed = data_type[3]
# print(mixed)

# # G. Create a list containing only negative even numbers from -2 to -12.
# negative = [-2, -4, -6, -8, -10, -12]

# # H. Create a list containing only positive even numbers from 0 to 12.
# positive = [2, 4, 6, 8, 10, 12]

# # I. Combine lists from Task G and H.
# combine = negative + positive
# print(combine)

# three = [3, 3, 3]

# # Create a new list containing the triple value of that list.
# triple_value = [value * 3 for value in three]
# print(triple_value)

# color = ["brown", "yellow", "white", "black", "green", "blue", "red"]
# print(color[-2:])

# original_list = [1, 2, 3, 4, 5]

# # Reverse the list using slicing
# r = original_list[::-1]

# # Print the reversed list
# print(r)

# in numerical contexts, True is treated as 1, and False is treated as 0.

# Get a list of numeric values from the user
# user_input = input("Enter a list of numeric values separated by spaces: ")

# Split the input into a list of strings
# numeric_strings = user_input.split()
# print(user_input)

# Example list
# my_list = [1, 2, 3, 4, 5]

# # Check if the list has at least one item
# if my_list:
#     print(True)
# else:
#     print(False)

# # Example list
# my_list = [1, 2, 3, 4, 5]

# # Print 'True' if there is at least one item in the list, 'False' otherwise
# print(bool(my_list))

# import random

# ran = [random.randint(5, -5) for _ in range(5)]
# ran.sort(reverse=True)
# print(ran[1])
# import random

# ran = [random.randint(5, -5) for _ in range(5)]
# ran.sort()
# print(ran[1])

# my_list = [1, 2, 3]
# my_list.insert(len(my_list), 4)
# print(my_list)

# import random

# print(random.random())

# my_list = [10, 20, 30, 40, 50]

# Remove the last element
# my_list.pop()

# print("Removed element:", last_element)
# print("Updated list:", my_list)
# print(my_list.pop())
# print(my_list)

# my_list = [10, 20, 30, 40, 50]

# Remove the last element using slicing
# my_list[:-1]
# my_list.pop(-1)
# print(my_list.pop(-1))
# print(my_list)

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# Concatenate using the += operator
# list1 += list2

# print("Concatenated list:", list1)
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# Concatenate using the * operator
# concatenated_list = [*list1, *list2]

# print("Concatenated list:", concatenated_list)
# print([*list1, *list2])

# my_list = [1, 2, 3, 4, 5] 
# result = my_list.find[2]
# print(result)

# letters = ['p', 'y', 't', 'h', 'o', 'n']
# print([letter.capitalize() for letter in letters])
# print(capitalize)
# print([letter.upper() for letter in letters])
# print(capitalize)

# colors = ["red", "blue", "green", "yellow", "orange"]
# print(colors * 2)
# duplicate = [color for color in colors for _ in range(2)]
# print(duplicate)

# my_list = [1, 2, 3, 4, 5] 
# result = my_list.index(3) 
# print(result)
# print(my_list[4])
# print(my_list)

# coordinates = (40.7128, -74.0060)
# latitude, longitude = coordinates
# print(latitude)
# print(longitude)
# latitude = (40.7128)
# longitude = (-74.0060)
# coordinates = latitude, longitude
# print(coordinates)
# print(latitude)
# print(longitude)

# my_tuple = (10, 20, 30, 40, 50)
# squared_tuple = (x**2 for x in range(1, 6))
# print(my_tuple)
# print(squared_tuple)

# 13. Which of the following list comprehensions creates a tuple of squares of numbers from 1 to 5?
#     = a) squared_tuple = (x ** 2 for x in range(1, 6))
#     b) squared_tuple = [x ** 2 for x in range(1, 6)]
#     c) squared_tuple = {x ** 2 for x in range(1, 6)}
#     = d) squared_tuple = (x ** 2 for x in [1, 2, 3, 4, 5])

# 22. How do you define a constant variable using a tuple in Python?
#     = a) constant_var = (value)
#     b) constant_var = [value]
#     c) constant_var = {value}
#     = d) constant_var = value

# length = int(input())
# width = int(input())
# perimeter = 2 * (length + width)
# print(perimeter)
# print(2 * (length + width))

# import math
# radius = int(input())
# area = math.pi * radius ** 2
# print(area)
# print(math.pi * radius ** 2)

# radius = int(input())
# pi = 3.14
# area = pi * radius ** 2
# print(area)
# print(pi * radius ** 2)

# """
# My name is Rasim
# """

# my_dict = {
#    'a': 1,
#    'b': 2,
#    'c': 3
# }
# print(my_dict.get('b'))

# my_dict = {
#    'a': 1,
#    'b': 2,
#    'c': 3
# }
# my_dict['d'] = 4
# print(my_dict)

# my_dict = {
#    'a': 1,
#    'b': 2,
#    'c': 3
# }
# print(list(my_dict.items()))

# my_dict = {
#    'a': 1,
#    'b': 2,
#    'c': 3
# }
# my_dict.pop('b')
# print(my_dict)

# my_dict = {
#    'a': 1,
#    'b': 2,
#    'c': 3
# }
# my_dict.update({'d': 5, 'e': 4})
# print(my_dict)
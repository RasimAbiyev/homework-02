# """
# - Strings -
# A. Create a variable called 'long_sentence'. Make it equal a sentence
# minimum. Print 'long_sentence's length.
long_sentence = "My name is Rasim"
print(len(long_sentence))

# B. Replace Print function's 'end' parameter from default '\n' to '\t'.
# Write 2 Print functions with it.
long_sentence = "I go to school"
print(long_sentence, end='\t')
print("I went to school")

# C. Change Print function's 'end' parameter, so that it links values with
# stars. Example:
# Today*is*a*good*day!
print("Today", "is", "a", "good", "day!", sep="*")

# D. Write 3 different Print functions with according string ("He", "is", "cool.")
# in such way so you can see this on your console (you can use any method):
# He is cool.
print("He", "is", "cool.")
print("He" + " is" + " cool.")
print("He", end=" ")
print("is", end=" ")
print("cool.")

# E. The same task as previous (D), but now make it look like:
# He#is#cool.
print("He", "is", "cool.", sep="#")

# F. Create a variable named 'color'. Give it a string 'Python' value.
color = "Python"

# G. Create a variable named 'item'. Give it a string 'Developer' value.
item = "Developer"

# H. Use all methods you know about string-formattings and Print function
# to concatenate these two variables, so you can see 'Python Developer' on your
# console (terminal).
print(f"{color} {item}")
print("{} {}".format(color, item))
print("%s %s" % (color, item))

# I. Replace Print function's 'end' parameter from default value to '...'.
# Write 3 Print functions with it.
print(color, item, end='...')
print(color, end=' ')
print(item, end='...')
print(color + ' ' + item, end='...')

# J. Suppose you have the following variable:
# word = "Hello. I am Taylor."
word = "Hello. I am Taylor."

# Using slicing method:
# 1. Create a variable called 'prefix'. Make it equal to 'Hello.' part of 'word' variable.
prefix = word[:6]
print(prefix)

# 2. Create a variable called 'middle_part'. Make it equal to ' I am ' part of 'word' variable.
middle_part = word[7:12]
print(middle_part)

# 3. Create a variable called 'name'. Make it equal to 'Taylor.' part of 'word' variable.
name = word[12:19]
print(name)

# Create a variable named 'recreated_word' or 'result' and use all previous variables 
# (prefix, middle_part, name) to recreate the 'word' phrase.
prefix = 'Hello.'
middle_part = ' I am '
name = 'Taylor.'
recreated_word = prefix + middle_part + name
print(recreated_word)

# K. Suppose you have the following value:
# "abababababa"
# Using slicing method, get all 'a' characters from the value and assign it to a
# variable, then print that variable.
a = "abababababa"
print(a[::2])

# L. Create a formula that finds the last index of a string.
a = "abababababa"
print(a[len(a)-1])
print(a[-1])

# M. What is the difference between 1 and "1"? Are they equal values, why?
int = 1
str = "1"

# N. Using all your Python knowledge, find the amount of words the following sentence:
# "The mission of the Python Software Foundation is to promote, protect, and advance 
# the Python programming language, and to support and facilitate the growth of a 
# diverse and international community of Python programmers."
sentence = "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers."
word_list = sentence.split()
num_words = len(word_list)
print(num_words)

# - String Methods -
# A. Use all these string methods and test it in your code:
# 1. title
sentence = "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers."
print(sentence.title())

# 2. capitalize
sentence = "the mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers."
print(sentence.capitalize())

# 3. count
sentence = "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers."
print(sentence.count("Python"))

# 4. endswith
sentence = "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers."
print(sentence.endswith("programmers."))

# 5. find
sentence = "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers."
print(sentence.find("Python"))

# 6. index
sentence = "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers."
print(sentence.index("Python"))

# 7. isalpha
sentence = "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers."
print(sentence.isalpha())

# 8. isdigit
sentence = "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers."
print(sentence.isdigit())

# 9. islower
sentence = "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers."
print(sentence.islower())

# 10. isupper
sentence = "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers."
print(sentence.isupper())

# 11. lower
sentence = "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers."
print(sentence.lower())

# 12. upper
sentence = "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers."
print(sentence.upper())

# 13. replace
sentence = "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers."
print(sentence.replace("Python", "Java"))

# 14. split
sentence = "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers."
print(sentence.split())

# 15. strip
sentence = "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers."
print(sentence.strip())

# 16. startswith
sentence = "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers."
print(sentence.startswith("The"))

# 17. join
sentence = "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers."
print(" ".join(sentence))

# B. Combine several string methods at once.
address = "123 MAIN ST APT 4B"
standardized_address = address.upper()
a = standardized_address.replace(" ", "")
print(a)


# C. Create any string-valued variable. First, call the 'lower' method on it,
# then call 'islower' method. What value will it always give you and why?
my_string = "Hello, World!"
lowercase_string = my_string.lower()
result = lowercase_string.islower()
print(result)

# D. Suppose you have the following variable:
# my_value = "Obviously, today is a hot day."
# Replace all 'o' characters with 0 (zeros). 
my_value = "Obviously, today is a hot day."
modified_value = my_value.replace('o', '0')
print(modified_value)

# E. Count how many times the word 'likes' occured in the following string:
# "Sammy likes to swim in the ocean, likes to spin up servers, and likes to smile."
my_string = "Sammy likes to swim in the ocean, likes to spin up servers, and likes to smile."
count_likes = my_string.count("likes")
print(count_likes)

# - String Formattings -
# A. Create a variable 'name' and assign your name to it.
# Create a variable 'age' and assign your age to it.
# Using the f-string method, create a formatted string that displays your name 
# and age in the following format:
# "My name is [name] and I am [age] years old."
name = "Rasim"
age = 29
print(f"My name is [{name}] and I am [{age}] years old.")

# B. Create a variable item and assign a string representing an item name.
# Create a variable quantity and assign an integer representing the quantity of the item.
# Create a formatted string using the old-style % formatting that displays the item 
# name and quantity in the following format:
# "I want to buy %d units of %s."
item = "trousers"
quantity = 25
print("I want to buy %d units %s." % (quantity, item))

# C. Make your best and create a hard task by your own using string formattings.
name = "Rasim"
age = 30
print("My name is {} and I am {} years old.".format(name, age))

# - Chat GPT's Homework -
# A. Use the len() function to find the length of the following strings:
# 1. "programming"
name = "programming"
print(len(name))

# 2. "python is fun"
name = "python is fun"
print(len(name))

# 3. "12345"
number = "12345"
print(len(number))

# B. Convert the following string to uppercase string:
name = "hello world"
print(name.upper())

# C. Check if the string "python" is present in the following sentence:
name = "I enjoy programming in Python."
print(name.find("python"))

# D. Given the string "programming", access the following elements using positive and negative indexing:
# 1. The first character
name = "programming"
print(name[0])

# 2. The last character
print(name[-1])

# 3. The third character
print(name[2])

# 4. The second-to-last character
print(name[1:11])

# E. Using string slicing, extract the word "is" from the string:
name = "Python is a versatile programming language."
print(name[7:9])

# F. Retrieve the substring "quick brown" from the following sentence:
name = "The quick brown fox jumps over the lazy dog."
print(name[4:15])

# G. Reverse the following string using slicing:
name = "redivider"
print(name[::-1])

# H. Write a program that capitalizes the first letter of each word in the following sentence:
name = "welcome to the world of programming"
print(name.title())

# - Interview Questions -
# A. Reverse any string using slicing method.
name = "Hello, World!"
print(name[::-1])

# B. Print the whole string using slicing method, not knowing the length of a string.
name = "Hello, World!"
print(name[:])

# - Comments -
# A. One-line comment in any random three places of your code, if it's appropriate.
# Hello

# B. Multi-line comment anywhere in your code, if it's appropriate.
""" My name is Rasim """

# Quiz:
# A. What does len('Hello ') return?
#     a) 4
#     b) 5
#     = c) 6
#     d) 'Hello'
#     e) "Hello"

# B. What is the output of the following code snippet:

#     sphere = "Web Development" * 2 + "" * 6
#     length = len(sphere)
#     print(length)

#     a) 15
#     b) 20
#     c) 25
#     = d) 30

# C. Which of the operator can be used in Strings?
#     a) +
#     b) *
#     = c) Both of the above
#     d) None of the above

# D. What is the output of the following code snippet:

#     comment = "I like your blue pants"
#     pattern = comment[19:4:-3]
#     print(pattern, len(pattern))

#     = a) "n lry", 5
#     b) "n lry", 4
#     c) "n ly", 4
#     d) "p ly", 4
#     e) "p l ", 4

# E. Is the following variable named correctly, why?

#     myVariable = "Python is best!"

#     a) yes, follows the rules of naming a variable, pythonic code
#     = b) no, doesn't follow the rules of naming a variable, non-pythonic code
#     c) it depends on the code editor you type
#     d) it's not a code written in Python
# """
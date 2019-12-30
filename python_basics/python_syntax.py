# Learning some python today 12/29/19 ------

# The octothorp is the symbol used for commenting out code.
# Comments are lines of code not read by the computer and has no
# interaction with the rest of the code. It's great if you want to
# put in notes about the code your'e working on for yourself and 
# other developers. 

# print()
# The print function is used to print a specified message to the
# screen or other standard output device.

print("Hello world!")

# The message inside the print function is a string literal.
# Strings are a data-type in python. Any block of code that is 
# wrapped in single or double quotes is considered a string.

# We can also assign our strings to variables. We use variables
# to store data. We assign values to our variables using the 
# assignment operator (=).

greeting = "Hi"

# Errors
# Humans are prone to errors and python will point out any errors
# you might make in the program by indicating the type of error
# and pointing out the location of the error with the (^) symbol.
# These errors are known as bugs and we as programmers must debug the
# errors to make the code run as intended (hopefully).

# Numbers
# Python has numeric data types which can be represented by:
# Whole numbers / Integers, known as (int)
# Decimals / Floating numbers, know as (float)

example_int = 10

example_float = 2.5

# Python can perfomr calculations ike addition, subtraction, multiplication
# and division. 

print(10 + 10) # addition
print(10 - 5) # subtraction
print(1 * 10) # multiplication
print(10 / 5) # division

# Concatenation in python is the process of combining two strings.
# ex:

first_name = "John "
last_name = "Doe"
print(first_name + last_name) # "John Doe"
print("Jane " + "Doe") # "Jane Doe"

# str() can be also be used to convert vatiables to strings.

age = 23

my_name_and_age = "Hello my name is " + first_name + "and I am " + str(age) + " years old."  

print(my_name_and_age)

# Plus Equals
# Python has a shorthand of (+=) which evaluates to var1 = var1 + var2

total_price = 10.99

new_item = 9.99

total_price += new_item

print(total_price)

# Multi-line strings
# By using 3 double or single quotes you can create a multi-line string

multi_line_string = """

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

"""
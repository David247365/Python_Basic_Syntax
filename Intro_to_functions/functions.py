# In simple terms a function in python is a tool that you can
# use over and over again to produce consistent output from 
# different inputs.

# Defining a function
def sing_song():
    print("Words fall, out of my mouth")
    print("They don't make a sound")
    print("and they drift to the ground")

sing_song()

# The keyword def tells Python that we are "defining" a function
# The function is called sing_song
# Everything that is indented after the (:) is what is 
# run when sing_song() is called.

def loading_screen():
    print("This page is loading...")

loading_screen()

# In python, the amount of whitespace tells the computer 
# what is part of a function and what is not.

# Parameters
# Parameters are variables that you can pass into the function
# when you call it.

                    #Parameter#
def greet_customer(special_item):
    print("Welcome!")
    print("Our special is " + special_item + ".")
    print("Thank you for shopping with us.")

# special_item is reffered to as a formal parameter.
# This is a placeholder for the value we would add into
# the function call

greet_customer("peanut butter")

# The value between the parantheses when we call the function
# is known as an argument of the function call.

# You can make your function take more than one paramater. You just need
# to seperate your parameters with commas. 

def multiply( a , b ):
    print(a * b)

multiply(10 , 20) # 200

# in multiply a and b are called positional arguments because their 
# assignments deend on their positions in the function call.

def add_two_nums(a, b):
    print(a + b)

# we can also pass these arguments as keyword arguments, where
# we explicitly refer to what each argument is assigned to the 
# function call.

add_two_nums(a = 2, b = 3)

# we can also use default arguments in our function. If the function is
# called without an argument for that parameter, it relies on the
# default.

def divide_two_nums(a, b = 2):
    print(a / b)

divide_two_nums(6) # Since we are only setting the argument for a, 
# b will automatically be defined as 2.

# Once you give an argument a default value, 
# no arguments that follow can be used positionally.


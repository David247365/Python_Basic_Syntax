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
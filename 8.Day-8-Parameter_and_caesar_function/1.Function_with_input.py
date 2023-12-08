# Function a block of code that accomplish or execute some task
# Function class Review

# 1:Create a function called greet()
def greet():
    # print 3 statement
    print("print1")
    print("Print2")
    print("Print3")


# call the function
greet()
# The above code output is constant whenever it is called.What about if we want a function to print different output based on input
# input with in a function   we will come in to some concept called arguement who accept input
'''
syntax 
def function_name(someInput):
    Do something with the input
'''


def greet_with_name(name):
    print(f"Hello {name}")


greet_with_name("Abebe")
# this is like assigning value to a variable
# name="Abebe" the variable known as parameter and the value is called arguement
# Challenge-1:Add another arguement


def greet_with_name_2(name, location):
    print(f"Hello {name} from {location}")


greet_with_name_2("anteneh", "AA")
# Reuse the function again and again
greet_with_name_2("kebede", "nazret")
# The above arguement is called the positional arguement because it does not associated with specific parameter so it consider the order of arguement and parameter

# Keyword arguement to be specific which arguement is for which parameter
# eg greeet_with_name_2(name="kebede", location="AA")
# The order or position will not be any matter eg
greet_with_name_2(location="Adama", name="Alemayehu")

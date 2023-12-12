#### Scope###
# scope is the span of a variable in which the variable is accessible to use its value
enemies = 1


def increase_enemies():
    enemies = 2
    # The above variable span time is limited to the end of this function:called local scope
    print(f"enemies inisde function:{enemies}")
    # The output is 2 access local variable enemies
    # If enemies variable is not updated the value remains the global variable


increase_enemies()
print(f"enemies outside the function{enemies}")
# The output is 1 it access from enemies var which present outside the span is all over the code(globally): global variable
# The only difference between the two variable is where they defined(outside function or inside function)

# There is no local scope in python:local variable is reside in function
# Example
name = ['a', 'b', 'c']


# def local_func():
if 3 > 2:
    new_name = name[1]
print(new_name)
# it print b
# if we insert the above code in to a function it will be local function and not accessible outside that function
# and says the variable is undefined

# Modifying the global  variable
name = 3


def modify_global():
    global name
    name = name+3
    print(name)


modify_global()

# It is useful to make some variable global specially constant in which value you do not need to change throughout the program

# Data type
# String:it is the data contain string of character.
# String Operation to get each letter(subscripting)
# Print O
print("Hello"[4])
# Any data inside the delimiter is considered as string
# eg in below code 123456 will be printed because they considered as string
print("123" + "456")

# Integer:All Whole number either posetive or negative
print(123+456)
# if it is big number we can use _ to deferenciate
num = 1_000_000
# The above is the same as 1M

# Float:It contains decimal point value
float_num = 3.14159

# Boolean:True or false Value
bool_val = True

# Note:For each data type there are a built in function that manipulate the date
# len():to know the length of the string
# print(len(input("enter your name")))
# type(): to know the type
print(type(True))


# Type casting:Changing the data type from one to another
str_int = int('12')
int_str = str(239)


# Challenge-1:Add the input digit
a = input(" \n")
first_digit = int(a[0])
second_digit = int(a[1])
print(first_digit + second_digit)

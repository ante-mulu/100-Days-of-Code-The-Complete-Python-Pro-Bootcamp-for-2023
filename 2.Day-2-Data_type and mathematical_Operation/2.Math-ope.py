# addition
add = 3+5
sub = 7-4
mul = 3*2
div = 6/3
power = 2**2
# Order is PEMDAS
print(3*3+3/3-3)

# Challenge-1:BMI Calculator formula bmi=w/h**2
# Note: The type we recieve from user is always str so we have to cast to other when mathimatical operation needed
# height = float(input())
# weight = float(input())

# bmi = int(weight/(height ** 2))
# print(bmi)


# Number Manipulation
# round(operation, decimal point) used to round in to specific floating point
print(round(8/3, 2))

# Floor Division: display quotient  eg 8//3 =2
print(8//3)
# update variable
score = 3
score = score + 1
# The hay way is to use +=
score += 1

# Note that we can only concatenate string value we can't contactenate string with integer
# The following code will generate typo error, we can fix this error by casting the value
print("my score is "+str(score))
# We can use f-string to concatenate different data type we can write the above code as below
print(f"my score is {score}")

# Challenge-2:
current_age = int(input("Enter your age"))
left_in_year = 90-current_age
print(f"You have left {52*left_in_year} left")

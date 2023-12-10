#Chabge version in 1.control flow
# if/else statement
# Depending on specific condition A or B will be executed
# checking whether the sink start or continue adding the water untill 90cm height
water_level = 50
if (water_level > 90):
    print("start sinking the water")
else:
    print("Continue")
# We check the condition using conditional comparison such as <,>,<=,>=,==,!=,===
# = assigning,== check the value in the left and right equal

# Challenge-1 check the number is even or odd
# Solution:We will use modulo operator
# What modulo operator does is in opposite to floor operation which return the quotient
'''input_number = int(input("Input the number you want to check"))
if (input_number % 2 == 0):
    print("The number is even")
else:
    print("The number is odd")'''

# Nested if elif statement:IF there are more than two condition we have to check we will use nested loop
# Eg:Wrting a code of roalcoster ticket which have different amount fee based on age and height must be >120
# height_input = int(input("Enter the height"))
# if height_input >= 120:
#     # He/she can enter next we check the fee Base om age
#     age = int(input("Enter the age"))
#     if age < 12:
#         print("pay $5")
#     elif age < 18:
#         print("pay $7")
#     else:
#         print("pay $12")
# else:
#     # he can not enter the game because of his height
#     print("You cant get in to the game, grow up and come back again")

# Challenge-2:BMI calculator and Interpretation of the result
# height = float(input("Enter your height in m: "))
# weight = float(input("Enter your weight in kg: "))
# bmi = Math.ceil(weight/(height**2))
# print("Your BMI is", bmi)
# if bmi < 18.5:
#     print("Under weight")
# elif bmi < 25:
#     print("Normal weight")
# elif bmi < 30:
#     print("Overweight")
# elif bmi < 35:
#     print("obese")
# else:
#     print("clinically obese")

# Challenge-3:Leap year:year%4==0,year%100!=0 and year%400!==0
# solution #2000%4==0,2000%100
#
# Note:The nested if else stop excuting the code once the condition fulfilled and only one of the condition will exicute

# Multiple if:all condition will be excuted
# Challenge-4:Pizza order
size = input("What size piza do you want?S,M,L")
add_pepperoni = input("do you neeed pepperoni?Y or N")
extra_cheese = input("Do you want extra cheese?Y,N")
if (size == "S"):
    bill = 15
    if (add_pepperoni == "Y"):
        bill = bill+2
    if (extra_cheese == "Y"):
        bill += 1
if (size == "M"):
    bill = 20
    if (add_pepperoni == "Y"):
        bill += 3
    if (extra_cheese == "Y"):
        bill += 1
if (size == "L"):
    bill = 25
    if (add_pepperoni == "Y"):
        bill += 3
    if (extra_cheese == "Y"):
        bill += 1
print(f"Your final bill is ${bill}")

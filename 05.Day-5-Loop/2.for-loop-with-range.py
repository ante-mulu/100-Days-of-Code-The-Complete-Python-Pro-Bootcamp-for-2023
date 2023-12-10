# range() is a function that returns number between to range and with for loop it is very important to loop thorough each number
# for num in range(0, 10):
#     print(num)
# the range doent include the last 10 and range is n-1
# Step we can add the 3rd arguement to tell the step or difference in value eg lets list a number in 3 step
# for n_3 in range(1, 10, 3):
#     print(n_3)
# number 1,4,7 displayed with difference of 3 in between

# Add the number from 1 to 100
# sum = 0
# for num in range(1, 101):
#     sum += num
# print(sum)
# Challenge-1:Print the sum of  n number
# n = int(input("Enter the number"))
# sum = 0
# for num in range(1, n+1):
#     sum = sum+num
# print(sum)
# Challenge-2:Fizbuzz
for number in range(1, 101):
    if (number % 3 == 0 and number % 5 == 0):
        print("FizzBuzz")
    elif (number % 3 == 0):
        print("Fizz")
    elif (number % 5 == 0):
        print("Buzz")
    else:
        print(number)

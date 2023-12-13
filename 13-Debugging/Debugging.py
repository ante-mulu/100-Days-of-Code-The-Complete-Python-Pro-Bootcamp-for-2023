############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()
#out of bound problem it needs be at least n+1 to include the number n
#to fix this proble we should add 1 to range 21

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 5)
# print(dice_imgs[dice_num])
#The list index starts from  0 and end length value-1 
#To fix we have to decrease range from 1 to 5

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?")
# # input method output is always return string value so we have to cast in to integer to compare with integer
# age=int(age)
# if age > 18:
#     print(f"You can drive at age {age}.")
#Error:IndentationError: expected an indented block and there must be letter f to use python f string

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# #this is the prople it should be assigning not equivalent
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#     #This is a prople append is out of the loop adn append the item only not into list so appending function is inserted in to for loop and it works
#   print(b_list)
# mutate([1,2,3,5,8,13])


#challenge-1:Even and odd
# number = int(input()) # Which number do you want to check?

# if number % 2 == 0:
#   #the error is setting = instead of ==
#   print("This is an even number.")
# else:
#   print("This is an odd number.")

# Which year do you want to check?
# year = input()
# #Casting
# year=int(year)
# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")



  #Challenge-2:Debugging FizzBuzz
target = int(input())
#UnExpected indent 
for number in range(1, target + 1):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print([number])
  
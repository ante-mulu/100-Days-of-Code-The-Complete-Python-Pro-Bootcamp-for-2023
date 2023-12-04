# List is a data structure(a way of organizing and storing data in a database)
# syntax listname =[item1,item2] the item can be different data type
# Challege-1:Banker Roulette
import random
#importing random module
# name_Strings = input("Enter the list of name: ").split(",")
# random_name = random.randint(0, len(name_Strings))
# print(f"{name_Strings[random_name-1]} is going to but the meal today")

# IndexError: happens when we try to access data beyond the last valid index
# Nested list:list inside a list
# eg
# first_four = ['A', 'B', 'C', 'D']
# next_four = ['E', 'F', 'G', 'H']
# FIRST_EIGHT = first_four+next_four
# print(FIRST_EIGHT)
# Challenge-2:Creating Thresure map
line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
# Where do you want to put the treasure?dx
position = input("Where do you want to put the treasure?dx: ")
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
if (position == "A1"):
    map[0][0] = 'X'
elif (position == "A2"):
    map[1][0] = 'X'
else:
    map[2][0] = 'X'

if (position == "B1"):
    map[0][1] = 'X'
elif (position == "B2"):
    map[1][1] = 'X'
else:
    map[2][1] = 'X'

if (position == "B1"):
    map[0][2] = 'X'
elif (position == "B2"):
    map[1][2] = 'X'
else:
    map[2][2] = 'X'
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")

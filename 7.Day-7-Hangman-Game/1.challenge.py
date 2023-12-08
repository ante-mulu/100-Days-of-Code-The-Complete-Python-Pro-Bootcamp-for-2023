# Step-1
import random
word_list = ["ardvark", "baboon", "camel"]

# TODO-1:Choose random word_from the word_list and assign to the variable
chosen_list = random.choice(word_list)
print(chosen_list)
# TODO-2:Ask user to guess a letter and assign their answer to a variable and make the guess lowercase
# guess = input("Enter the letter").lower()
# for i in range(len(chosen_list)):
#     if guess in chosen_list[i]:
#         print("Right")
#     else:
#         print("Wrong")
#     i += 1

# Step-2
# TODOS-1:Create an empty list called display
display = []
# for i in range(len(chosen_list)):
#     print("_", end=" ")
guess = input("guess letter: ").lower()

# Todo-2:loop through each position in each word
# for i in range(0, len(chosen_list)):
#     if guess == chosen_list[i]:
#         display.append(chosen_list[i])
#     else:
#         display.append("_")
# print(display)
# Todo-3:Print Display list
for i in range(0, len(chosen_list)):
    if guess == chosen_list[i]:
        display = chosen_list[i]
        print(display, end="")
    else:
        print("_", end="")

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
# guess = input("guess letter: ").lower()
# Todo-2:loop through each position in each word
# for i in range(0, len(chosen_list)):
#     if guess == chosen_list[i]:
#         display.append(chosen_list[i])
#     else:
#         display.append("_")
# print(display)
# Todo-3:Print Display list
# for i in range(0, len(chosen_list)):
#     if guess == chosen_list[i]:
#         display = chosen_list[i]
#         print(display, end="")
#     else:
#         print("_", end="")
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
# Step-3:Checking if the player has won
for i in range(0, len(chosen_list)):
    display.append("_")
print(display)
lives = 6  # Re arranged from step-4
i = 0
while (i < len(chosen_list)):
    guess = input("Guess a letter: ").lower()
    if guess == chosen_list[i]:
        display[i] = chosen_list[i]
    else:
        lives -= 1
    
        while(lives>0)
        if not lives < 0:
            print(stages[lives])
    i += 1
    print(display)
if lives == 0:
    print("You Lose")
display_letter = ""
for letter in display:
    display_letter += letter
if display_letter == chosen_list:
    print("You won")

# Step-4:
# Step 4

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.

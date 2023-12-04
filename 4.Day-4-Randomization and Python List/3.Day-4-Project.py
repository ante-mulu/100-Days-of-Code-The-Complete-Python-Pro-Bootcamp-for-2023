import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
user_choice = int(input(
    "what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
RPS = [rock, paper, scissors]
print(RPS[user_choice])
random_rps = random.choice(RPS)
random_rps_index = RPS.index(random_rps)
print(f"Computer chose:\n")
print(RPS[random_rps_index])

if ((user_choice == 0 and random_rps_index == 2) or (user_choice == 1 and random_rps_index == 0) or (user_choice == 2 and random_rps_index == 1)):
    print("You win!")
elif (user_choice == random_rps_index):
    print("It's a draw.")
else:
    print("You lose")

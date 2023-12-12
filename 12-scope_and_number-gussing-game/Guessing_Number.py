import random
print("Welcome to number Guessing")
initial_num = 1
last_number = 101
print(f"I am thinking of the number between {initial_num} and {last_number-1}")
hard_try_chance = 5
easy_try_chance = 10
end = False
choose_level = input("Enter the level of the game: 'easy' or 'hard'")
random_number = random.randint(initial_num, last_number)

if choose_level == "easy":
    while not end:
        guess_num = int(input("Guess the number"))
        if guess_num < 100 and guess_num >= 1:
            if guess_num == random_number:
                print(f"The number is {guess_num} you got the answer")
                end = True
            else:
                if guess_num > random_number:
                    print("Too high")
                else:
                    print("Too Low")
                easy_try_chance -= 1
                if easy_try_chance == 0:
                    print("You finished your trial")
                    end = True
                print(f"You have more {easy_try_chance}")
        else:
            print("The number is out of range")

else:
    while not end:
        guess_num = int(input("Guess the number"))
        if guess_num > 1 and guess_num <= 100:
            if guess_num == random_number:
                print(f"The number is {guess_num} you got the answer")
                end = True
            else:
                if guess_num > random_number:
                    print("Too high")
                else:
                    print("Too Low")
                hard_try_chance -= 1
                print(f"You have more {hard_try_chance}")
            if hard_try_chance == 0:
                print("You finished your trial")
                end = True
        else:
            print("The number is out of range")
            end = True

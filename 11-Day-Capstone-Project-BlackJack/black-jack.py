import os
import art
import random
'''
The goal of blackjack is to have a hand total as close to 21 as possible without going over.

-----Value----
        -->Each numbered card (2-10) is worth its face value. 
        -->Face cards (Jacks, Queens, and Kings) are worth 10. 
        -->Aces can be worth 1 or 11, whichever is better for the player.

---Game---
        The game starts with 
            -->the dealer giving each player two cards facing up. 
            -->The dealer also gets two cards, one facing up and one facing down.
--options--
        -->"Hit" to get another card to increase their total.
        -->"Deal" if they are satisfied with their hand.
'''
Want_to_stop_play = False
card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
play_card_me = [random.choice(card), random.choice(card)]
computer_card = [random.choice(card)]
while not Want_to_stop_play:
    print(f"Your card:{play_card_me}")
    print(f"Computer card:{computer_card}")
    add_card = input(
        "Type y to get another card type 'n' to pass (y/n)").lower()
    if add_card == "n":
        final_card_me = play_card_me
        computer_card.append(random.choice(card))
        final_card_computer = computer_card
    print(f"Your final hand: {final_card_me}")
    print(f"Computer final hand: {final_card_computer}")

    # Calculating the sum of each hand
    sum_me = 0
    for my_card_score in final_card_computer:
        sum_me = sum_me+my_card_score
    sum_computer = 0
    for computer_card_score in final_card_computer:
        sum_computer = sum_computer+computer_card_score

        # Rule
        '''
            If a player's total goes over 21, they lose immediately (called a "bust"). 
            If the dealer goes over 21, all remaining players win.
            Once the dealer finishes, the player's and dealer's hands are compared. The player with a hand closer to 21 wins. 
            If the player and dealer have the same total, it's a tie.
            If a player's first two cards are an Ace and a card worth 10 (10, Jack, Queen, or King), they have a "blackjack" and usually win at a higher payout rate.
        '''
    goal = 21
    if (sum_computer > 21 and sum_me > 21):
        print("Bust")
    elif (sum_computer > 21):
        print("You win")
    elif (sum_me > 21):
        print("You lose")
    elif (sum_computer == sum_me):
        print("tie")
    else:
        dis_from_me_to_goal = 21-sum_me
        dis_from_computer_to_goal = 21-sum_computer
        if (dis_from_me_to_goal < dis_from_computer_to_goal):
            print("You win")
        else:
            print("The computer win")
            more_game = input("Do you want to play blackjack?Y,N").lower()
            if more_game == 'y':
                Want_to_stop_play = True

    if add_card == "y":
        os.system("cls")
        print(art.logo)
        play_card_me.append(random.choice(card))
        os.system("cls")
        print(play_card_me)

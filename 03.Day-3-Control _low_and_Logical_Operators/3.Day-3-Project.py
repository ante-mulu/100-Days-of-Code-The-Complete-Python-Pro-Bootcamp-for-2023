# Treasure
# Amend the commit
print("Your mission is to find a treasure: ")
road_direction = input(
    'You are at cross road.Where do you want to go? type "left" or "right: "').capitalize()
swim = input('Swim or not').capitalize()
door_color = input('which door Red,Yellow or blue: ').capitalize()
if (road_direction == "Left"):
    # Continue with game next choice
    if (swim == "Wait"):
        # Continue with game next choice
        if (door_color == "Yellow"):
            print("You win")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")

from art import logo,vs
print(logo)
from game_data import data
import random
fail=False
score=0
while not fail:
    rand_index_A=random.randint(0,len(data)-1)
    print(f"Compare A: {data[rand_index_A]['name']} a {data[rand_index_A]['description']} from {data[rand_index_A]['country']}")
    rand_index=random.randint(0,len(data)-1)
    if(rand_index!=rand_index_A):
        rand_index_B=rand_index
    print(vs)
    print(f"Compare B: {data[rand_index_B]['name']} a {data[rand_index_B]['description']} from {data[rand_index_B]['country']}")
    Guess=input("Which has more follower? Type 'A' or 'B' ")
    if (Guess=='A' and data[rand_index_A]['follower_count'] >data[rand_index_B]['follower_count']) or (Guess=='B' and data[rand_index_B]['follower_count'] >data[rand_index_A]['follower_count']):
        score=score+1
    else:
        fail=True
print(f"Score:{score}")
    





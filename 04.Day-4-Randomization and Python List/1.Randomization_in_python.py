# Used to create a computer program that have no a degree of un pridictability
# Random Integer between 0 and 1
import random
# import pi_module
# rand_number = random.random()
# print(rand_number)
# # Random integer
# rand_int = random.randint(1, 10)
# print(rand_int)
# # Random float between two int
# random_float = 5*random.random()
# print(random_float)

# list_of_words = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
# random_word = random.choice(list_of_words)
# print(random_word)
# # random is a python module to get random value
# # Module means a set of file with some functionality and value
# # eg We created pi_module.py file that hold the value of pi
# print(pi_module.pi)

# Challenge-1:Head and tail
rand_num = random.randint(0, 1)
if rand_num == 1:
    print("Heads")
else:
    print("Tails")

head_tail = ['Heads', 'Tails']
rand_list = random.choice(head_tail)
print(rand_list)

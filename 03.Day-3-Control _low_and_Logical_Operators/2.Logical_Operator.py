# We use operator if we want Checking multiple condition in the same line of code(Combining different operator)
'''
There are mainly 3 basic logical operator
A and B:True if Both Condition True
C or D:True if one of them is true
not E:True for false and vise vers a
'''
# Challege-1:Love calculator
name1 = input("What is your name \n").upper()
name2 = input("What is their name? \n").upper()
name_combined = name1+name2
T = name_combined.count("T")
R = name_combined.count("R")
U = name_combined.count("U")
E = name_combined.count("E")

L = name_combined.count("L")
O = name_combined.count("O")
V = name_combined.count("V")
E = name_combined.count("E")

print(f"T:{T}  L:{L}")
print(f"R:{R}  O:{O}")
print(f"U:{U}  V:{V}")
print(f"E:{E}  E:{E}")
print("------  -----")
print(f"{T+R+U+E} {L+O+V+E} %")

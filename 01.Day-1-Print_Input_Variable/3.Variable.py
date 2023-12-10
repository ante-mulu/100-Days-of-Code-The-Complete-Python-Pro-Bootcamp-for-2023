# Variable:A reserved Memory Location to store data
# Challenge-1
# There are two variables, a and b from input
a = input()
b = input()
# 🚨 Don't change the code above ☝️
####################################
# Write your code below this line 👇
# Solution This is about swapping a value between two variable in input a=30 b=20 but in display a=20 and b=30
# Let as create a new temporary variable

c = b
b = a
a = c

'''With out 3rd Variable
let say a=20 b=30
a=a+b
a=20+30(50)
b=a-b
b=50-30(20)
a=a-b
a=50-20(30)
The final result is a=30 and b=20'''

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

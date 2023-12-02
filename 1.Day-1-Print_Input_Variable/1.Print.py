# Challenge-1: print all three lines
# Day 1 - Python Print Function
# The function is declared like this:
# print('what to print')
# Solution

# line-1
print("Day 1 - Python Print Function")
# line-2
print("The function is declared like this:")
# line-3
print("print('what to print')")

'''Note:we can use double and single quotes alternatively as a delimiter.
The question is what if both of them used as string delimiter and value like this:print("print("double qoute in side double qoute delimiter")"
print("print("double qoute")")   SyntaxError: invalid syntax. Perhaps you forgot a comma?
to fix this we have to wrap single qoute  in side double qoute delimiter or vice versa change the " double qoute" 'double qoute'
print("print('double qoute'))") 
'''
# printing in separate file using \n
print("Hello world!\nHello world! \nHello world!")
# String Concatenation:Combining(Merging) different string so that they will be added together
# The above code combining string "Hello"," ", and "World" and output is Hello world!
print("Hello"+" " + "World!")

# Challenge:2:debugging(pick out of moth😂)
'''
Fix the code below 👇
print(Day 1 - String Manipulation")
print("String Concatenation is done with the "+" sign.")
  print('e.g. print("Hello " + "world")')
print(("New lines can be created with a backslash and n.")'''

# Line-1:The bug is because of the absence of delimiter so can be solve by adding these delimiter
print("Day 1 - String Manipulation")
# Line-2:the output needed is to display "+"" this output could be found by adding the following
print("String Concatenation is done with the" + '"+"' + "sign.")
# Line-3:This is indentation error so deleting a space at the beginning will solve the problem
print('e.g. print("Hello " + "world")')
# line-4:This is the syntax error in ( is unneccessary so we remove this
print("New lines can be created with a backslash and n.")

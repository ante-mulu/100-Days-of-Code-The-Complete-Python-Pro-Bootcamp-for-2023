# from turtle import Turtle,Screen
# timmy = Turtle()
# timmy.shape("turtle")
# my_screen =Screen()

# #challenge-1:Changing the color from default to red
# timmy.color("DarkGreen")
# #Challenge-2:Move the turtle by 100 paces
# timmy.forward(100)
# timmy.backward(200)
# my_screen.exitonclick()

#Installing python package from pypi
#using command line pip install -U prettytable


#challenge-3:Create a preetyTable object and save it to a table variable
from prettytable import PrettyTable
table =PrettyTable()
# table.field_names = ["Pokemon Name", "Type"]
#Challenge-4: Create two column adn add 3 data on it
table.add_column("Polemon Name",["Pikachu","Squitle", "Charmander"])
table.add_column("Type",["Electric","Water", "fire"])


#Challenge-5:Change the default attribute 
#Change the table allignment from center to right
table.align ="r"
print(table)


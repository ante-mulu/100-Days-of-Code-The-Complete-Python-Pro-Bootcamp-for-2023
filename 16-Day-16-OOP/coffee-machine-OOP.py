from CoffeMachineClass import CoffeMachine
# creating instance of all hot drink
espresso = CoffeMachine()
espresso.MENU={
        "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    }
}
latte= CoffeMachine()
latte.MENU={
        "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        }
}}
cappucino = CoffeMachine()
cappucino.MENU ={
        "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


all_resource =CoffeMachine()
all_resource.resources={
"water": 300,
"milk": 200,
"coffee": 100,
"Money":0
}
report =CoffeMachine()

off=False
while not off:
    user_menu = input("What Would you like?(esperroso/latte/capuccino) ").lower()
    if user_menu == "report":
        report.report(all_resource.resources)
    elif user_menu == "espresso":
        espresso.Coin_Process(all_resource.resources)
        espresso.transaction_status(all_resource.resources,user_menu,espresso.MENU)
    elif user_menu == "latte":
        latte.Coin_Process(all_resource.resources)
        latte.transaction_status(all_resource.resources,user_menu,latte.MENU)
    elif user_menu == "cappuccino":
        cappucino.Coin_Process(all_resource.resources)
        cappucino.transaction_status(all_resource.resources,user_menu,cappucino.MENU)
    elif user_menu == "off":
        off=True
    else:
        print("Incorrect input please try again")


          


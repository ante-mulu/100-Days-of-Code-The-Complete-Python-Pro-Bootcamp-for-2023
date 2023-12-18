MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
resources["Money"]=0
def report():
    for key, value in resources.items():
        print(f"{key}: {value}")
def Coin_Process():
    print("Please Insert the coin: ")
    pennies = float(int(input("How many Pennies: "))*0.01)
    dimes = float(int(input("How many Dimes"))*0.1)
    nickles = float(int(input("How many nickles"))*0.05)
    quarter = float(int(input("How many Quarter"))*0.25)
    coin_processed =quarter + dimes+ nickles + pennies
    print(f"Here is your {coin_processed} exchange")
    resources["Money"]+=coin_processed
    return coin_processed
def transaction_status(user_menu):
    Exchange_coin =Coin_Process()
    if user_menu=="espresso":
        if resources["water"]>MENU[user_menu]["ingredients"]["water"] and resources["coffee"]>MENU[user_menu]["ingredients"]["coffee"] and resources["Money"]>MENU[user_menu]["cost"]:
            print(f"here is your{user_menu} enjoy it")
            resources["water"]-=MENU[user_menu]["ingredients"]["water"]
            resources["coffee"]-=MENU[user_menu]["ingredients"]["coffee"]
            resources["Money"]-=MENU[user_menu]["cost"]

        elif not resources["water"]>MENU[user_menu]["ingredients"]["water"]:
            print(f"There is no enough water") 
        elif not resources["coffee"]>MENU[user_menu]["ingredients"]["coffee"]:
            print(f"There is no enough coffee") 
        elif not resources["coffee"]>MENU[user_menu]["ingredients"]["coffee"]:
            print(f"There is no enough coffee")
        elif not resources["Money"] > MENU[user_menu]["cost"]:
            print("In sufficient Balance. Money Refunded")
    elif user_menu =="latte" or user_menu=="cappucino":
        if resources["water"]>MENU[user_menu]["ingredients"]["water"] and resources["milk"]>MENU[user_menu]["ingredients"]["milk"]  and resources["coffee"]>MENU[user_menu]["ingredients"]["coffee"] and resources["Money"]>MENU[user_menu]["cost"]:
            print(f"here is your{user_menu} enjoy it")
            resources["water"]-=MENU[user_menu]["ingredients"]["water"]
            resources["milk"]-=MENU[user_menu]["ingredients"]["milk"]
            resources["coffee"]-=MENU[user_menu]["ingredients"]["coffee"]
            resources["Money"]-=MENU[user_menu]["cost"]
        elif not resources["water"]>MENU[user_menu]["ingredients"]["water"]:
            print(f"There is no enough water") 
        elif not  resources["milk"]>MENU[user_menu]["ingredients"]["milk"]:
            print(f"There is no enough milk") 
        elif not resources["coffee"]>MENU[user_menu]["ingredients"]["coffee"]:
            print(f"There is no enough coffee") 
        elif not resources["coffee"]>MENU[user_menu]["ingredients"]["coffee"]:
            print(f"There is no enough coffee")
        elif not resources["Money"]> MENU[user_menu]["cost"]:
            print("In sufficient Balance. Money Refunded")  


while True:
    user_menu = input("What Would you like?(esperroso/latte/capuccino) ").lower()
    if user_menu == "report":
        report()
    elif user_menu == "espresso":
        transaction_status(user_menu)
    elif user_menu == "latte":
        transaction_status(user_menu)
    elif user_menu == "cappuccino":
        transaction_status(user_menu)
    else:
        print("Incorrect input please try again")
    
        





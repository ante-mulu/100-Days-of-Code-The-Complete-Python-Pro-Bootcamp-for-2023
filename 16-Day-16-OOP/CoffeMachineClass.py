class CoffeMachine:
#What it has
    
    MENU ={}
    User_choice=''
    resources={}
    def Coin_Process(self,resources):
        print("Please Insert the coin: ")
        pennies = float(int(input("How many Pennies: "))*0.01)
        dimes = float(int(input("How many Dimes"))*0.1)
        nickles = float(int(input("How many nickles"))*0.05)
        quarter = float(int(input("How many Quarter"))*0.25)
        coin_processed =quarter + dimes+ nickles + pennies
        print(f"Here is your {coin_processed} exchange")
        resources["Money"]+=coin_processed
        return coin_processed
    
    def transaction_status(self,resources,user_menu,MENU):
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

    def report(self, resources):
        for key, value in resources.items():
            print(f"{key}: {value}")



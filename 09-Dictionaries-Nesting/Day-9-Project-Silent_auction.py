import os
print("Welcome to the secret auction program")
bider_dic = {
    "Name": [],
    "bid": []
}
other_bidder = False
while not other_bidder:
    name = input("What is your name: ")
    bid = int(input("What is your bid in $: "))
    bider_dic["Name"].append(name)
    bider_dic["bid"].append(bid)
    other_bid = input("are there any other bidders?yes,no")
    if other_bid == "no":
        other_bidder = True
    if other_bid == "yes":
        os.system("cls")
i = 0
while i < len(bider_dic["bid"]):
    max_bid = bider_dic["bid"][0]
    if bider_dic["bid"][i] > max_bid:
        max_bid = bider_dic["bid"][i]
    i += 1
print(
    f"The winner is {bider_dic['Name'][bider_dic['bid'].index(max_bid)] } with the bid {bider_dic['bid'][bider_dic['bid'].index(max_bid)]}$")

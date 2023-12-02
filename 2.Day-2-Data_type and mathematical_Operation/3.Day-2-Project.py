bill = float(input("Enter the total bill:"))
tip = int(input("tip in %:10,12 or 15"))/100
number_people = int(input("Number of People:"))
bill_per_person = bill/number_people
total_cost = tip + bill_per_person
print(f"Bill per person is {round(total_cost,2)}")

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

bill_with_percentage = ((percentage * bill) / 100) + bill

bill_each_people = round(bill_with_percentage / people, 2)

message = (f'Each person should pay: ${bill_each_people}')
print(message)

print("Welcome to the tip calculator.")


bill = float(input("What was the total bill? $"))
percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

bill_with_percent = ((percent * bill) / 100) + bill
bill_each_people = round(bill_with_percent / people, 2)
final_bill = "{:.2f}".format(bill_each_people)

message = (f'Each person should pay: ${final_bill}')

print(message)

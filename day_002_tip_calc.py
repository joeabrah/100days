print("Welcome to the tip calculator")

bill = input("What was the total bill?")
tip_percent = input("What percentage tip would you like to give? 10, 12, 15, or 20?")
num_people = input("How many people are there to split the check with?")

tip_amount = int(tip_percent)/100 * int(bill)
total_bill = int(bill) + tip_amount
bill_per_person = total_bill / int(num_people)

print(f"Each person should pay {bill_per_person}")

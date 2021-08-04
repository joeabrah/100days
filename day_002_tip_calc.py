#Prints the welcome message
print("Welcome to the tip calculator")

#Add the inputs with defined data types for each
bill = float(input("What was the total bill?"))
tip_percent = int(input("What percentage tip would you like to give?"))
num_people = int(input("How many people are there to split the check with?"))

#Convert the inputs to usable data
tip_amount = (tip_percent/100) * bill
total_bill = bill + tip_amount

#Figures the bill per person, rounding to the nearest 2 decimal points, and fixes decimal formatting with trailing zeros
bill_per_person = round((total_bill / num_people), 2)
bill_per_person = "{:.2f}".format(bill_per_person)

#Print the results using a f-string (function is inside of stringusing {})
print(f"Each person should pay ${bill_per_person}")

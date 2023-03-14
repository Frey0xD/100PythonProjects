
# if the bill was $150.00 split between 5 people with 12% tip 
# each person whould pay (150.00/5) * 1.12

print("Welcome to the tip calculator")

bill = float(input("What was the total bill :-$"))

tip_per = int(input("What percentage tip would you like to give ? 10,12, 15 ? :-"))

people = int(input("How many number of perople to split bill :-?"))

#tip = int(tip_per) / 100
#amount = float(bill) * tip
#final = float(bill) + amount

#print("Total Amount you have to pay:-" + str(final))

bill_per = tip_per / 100
total_amount = bill * bill_per
total_bill = bill + total_amount
#Bill per person (BPP)
BPP = total_bill / people
final_amount= round(BPP,2)
print(f"Each person should pay ${final_amount}")

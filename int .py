print("Welcome to the tip calculator!")
bill = float(input("What was your total bill?"))
tip = int(input("How much tip would you like to give? 10, 12, 15? "))
people = int(input("How much people to split the bill?"))
bill_with_tip = tip / 100 * bill + bill 
total_bill = bill_with_tip
bill_per_person = total_bill / people
final_amount =round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")
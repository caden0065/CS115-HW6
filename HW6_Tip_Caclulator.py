"""
caden crose
2/18/2026
a program that calculates a tip
and how you should split the bill
"""

# start message

print('Hello. To calculate your tip, input your information when prompted.')
print('For correct use, make sure to only enter digits. Do not spell out the answers.')
print()

# input

# bill total
billTotal = float(input("What was your total bill total? $ "))
print()
# tip percentage
tipAmount = float(input("What percentage would you like to tip? "))
print()
# splitting bill
splitBill = int(input("How many people will be paying for the bill (split evenly)? "))

# calculations

# amount to tip
tipTotal = round((tipAmount / 100) * billTotal, 2) # rounded to 2 decimals
# total bill (with tip)
newBillTotal = tipTotal + billTotal
# splitting the bill per person
splitTotal = newBillTotal / splitBill

# output

print()
# tip total with new bill amount
print(f'Your tip will be ${tipTotal}, that means your new bill will be ${newBillTotal}.')
# split bill costs
print(f'To split the bill between {splitBill} people, you will pay ${splitTotal} per person.')


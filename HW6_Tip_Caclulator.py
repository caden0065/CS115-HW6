"""
caden crose
2/18/2026
a program that calculates a tip
and how you should split the bill
"""

print('Hello. To calculate your tip, input your information when prompted.')
print('For correct use, make sure to only enter digits. Do not spell out the answers.')
print()

billTotal = float(input("What was your total bill total? $ "))
print()
tipAmount = float(input("What percentage would you like to tip? "))
print()
splitBill = int(input("How many people will be paying for the bill (split evenly)? "))

tipTotal = round((tipAmount / 100) * billTotal, 2)
newBillTotal = tipTotal + billTotal

splitTotal = newBillTotal / splitBill

print()
print(f'Your tip will be ${tipTotal}, that means your new bill will be ${newBillTotal}.')
print(f'To split the bill between {splitBill} people, you will pay ${splitTotal} per person.')


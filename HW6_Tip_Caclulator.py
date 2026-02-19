"""
caden crose
2/18/2026
a program that calculates a tip
and how you should split the bill
"""

# start message

print("-- Tip Calculator --")
print("Hello. To calculate your tip, input your information when prompted.")
print("For correct use, make sure to only enter digits. Do not spell out the answers.")
print()

# input

# handle incorrect input for bill amount and tip amount
def get_float(prompt):
    while True:
        user = input(prompt).strip()
        try:
            return float(user)
        except ValueError:
            print()
            print("Please type a number (example: 12.50).")

# handle incorrect input for splitting bill
def get_int(prompt):
    while True:
        user = input(prompt).strip()
        try:
            value = int(user)
            if value < 1:
                print()
                print("Please enter a number equal to or higher than 1.")
                continue
            return value
        except ValueError:
            print()
            print("Please type a whole number (example: 2).")

# bill total
billAmount = get_float("How much was your bill? $ ")
print()
# tip percentage
tipAmount = get_float("What percentage would you like to tip? % ")
print()
# splitting bill
splitBill = get_int("How many people will be paying for the bill (split evenly)? ")

# calculations
    # (round() rounded it to 2 decimals)

# amount to tip
tipTotal = round((tipAmount / 100) * billAmount, 2)
# total bill (with tip)
newBillTotal = round(tipTotal + billAmount, 2)
# splitting the bill per person
splitTotal = round(newBillTotal / splitBill, 2)

# output
    # (.2f keeps 2 decimal places even if 0)

print()
print()
print("-- Bill Summary --")
print()
print(f"Bill: ${billAmount:.2f}")
print(f"Tip: ${tipTotal:.2f}")
print(f"Total: ${newBillTotal:.2f}")
print(f"Split {splitBill} ways: ${splitTotal:.2f}")
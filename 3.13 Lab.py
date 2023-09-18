# Lab 3.13 - Exact Change
# Take an input as an int
change_input = int(input())

# Print 'No change' if the user inputs zero or less
if change_input <= 0:
    print('No change')

# See how many dollars, quarters, dimes, nickles, and pennies go into the total using a modulo
elif change_input >= 1:
    dollars = change_input // 100
    change_input %= 100
    quarters = change_input // 25
    change_input %= 25
    dimes = change_input // 10
    change_input %= 10
    nickels = change_input // 5
    change_input %= 5
    pennies = change_input

# Print the number of relevant coins
    if dollars:
        if dollars > 1:
            print(f'{dollars} Dollars')
        else:
            print("1 Dollar")
    if quarters:
        if quarters > 1:
            print(f'{quarters} Quarters')
        else:
            print("1 Quarter")
    if dimes:
        if dimes > 1:
            print(f"{dimes} Dimes")
        else:
            print("1 Dime")
    if nickels:
        if nickels > 1:
            print(f"{nickels} Nickels")
        else:
            print("1 Nickel")
    if pennies:
        if pennies > 1:
            print(f"{pennies} Pennies")
        else:
            print("1 Penny")

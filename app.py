# Creates a program which calculates the down payment of a real estate project
house_price = 1000000
has_good_credit = True
has_high_income = True
if has_good_credit or has_high_income:
    print("Eligible for loan")
    if has_good_credit:
        down_payment = house_price * 0.1

    else:
        down_payment = house_price * 0.2
else:
    print("Not eligible for loan")


print("The downpayment required to be paid is $" + str(down_payment))
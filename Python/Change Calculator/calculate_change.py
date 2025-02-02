
import pprint

def calculate_change(item_price, amount_paid):

    # calculate difference between item price and amount paid
    change_due = round(amount_paid - item_price, 2)

    # work out if change is owed
    if change_due < 0:
        print("Not enough £ has been paid.")
        return
    elif change_due == 0:
        print("Exact amount paid. No change owed.")
        return
    else:
        print(f"Amount of change owed: £{change_due}")

    # list of accepted denominations
    denominations = {20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.5: 0, 0.2: 0, 0.1: 0, 0.05: 0, 0.02: 0, 0.01: 0}

    # loop through each denomination and calculate the number of each denomination to give through integer division
    for denomination in denominations.keys():
        quantity = change_due // denomination
        
        change_due = round(change_due - quantity * denomination, 2)
    
        denominations[denomination] = quantity

    # subtract the multiple from the change owed
    pprint.pp(denominations)

calculate_change()